# -*- coding: utf-8 -*-
"""
Finance Repository - Data access layer for student invoices and payments
"""

import json
from datetime import datetime
from typing import List, Dict, Optional, Any
from ..database import get_db_connection

class FinanceRepository:

    @staticmethod
    def get_all_invoices() -> List[Dict[str, Any]]:
        """Fetch all invoices with student details."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT i.*, s.full_name as student_name, s.college
        FROM invoices i
        JOIN students s ON i.student_id = s.student_id
        ORDER BY i.invoice_number DESC;
        """)
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def get_student_ledger(student_id: str) -> Dict[str, Any]:
        """Fetch financial statement for a specific student."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?;", (student_id,))
        student = cursor.fetchone()
        if not student:
            conn.close()
            return None

        cursor.execute("SELECT * FROM invoices WHERE student_id = ? ORDER BY invoice_number DESC;", (student_id,))
        invoices = [dict(r) for r in cursor.fetchall()]
        conn.close()

        total_invoiced = sum(i['total_payable_qar'] for i in invoices)
        total_paid = sum(i['paid_amount_qar'] for i in invoices)
        outstanding = max(0.0, total_invoiced - total_paid)

        return {
            "student_id": student_id,
            "full_name": student["full_name"],
            "outstanding_balance_qar": outstanding,
            "total_invoiced_qar": total_invoiced,
            "total_paid_qar": total_paid,
            "invoices": invoices
        }

    @staticmethod
    def process_payment(invoice_number: str, student_id: str, amount: float) -> Optional[Dict[str, Any]]:
        """Apply a payment to an invoice and reconcile student holds."""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM invoices WHERE invoice_number = ? AND student_id = ?;", (invoice_number, student_id))
        inv = cursor.fetchone()
        if not inv:
            conn.close()
            return None

        new_paid = min(inv['total_payable_qar'], inv['paid_amount_qar'] + amount)
        status = 'مدفوع كلياً' if new_paid >= inv['total_payable_qar'] else 'مدفوع جزئياً'
        txn_ref = f"QPAY-TXN-{int(datetime.now().timestamp())}"
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
        UPDATE invoices
        SET paid_amount_qar = ?, payment_status = ?, payment_reference = ?, payment_date = ?
        WHERE invoice_number = ?;
        """, (new_paid, status, txn_ref, now_str, invoice_number))

        # Re-check remaining balance
        cursor.execute("""
        SELECT SUM(total_payable_qar - paid_amount_qar) as rem_due
        FROM invoices WHERE student_id = ?;
        """, (student_id,))
        row = cursor.fetchone()
        rem_due = max(0.0, float(row['rem_due'] if row['rem_due'] is not None else 0.0))

        # Update holds
        cursor.execute("SELECT active_holds FROM students WHERE student_id = ?;", (student_id,))
        st = cursor.fetchone()
        holds = json.loads(st['active_holds']) if st['active_holds'] else []
        if rem_due <= 0.0 and 'Financial' in holds:
            holds.remove('Financial')

        cursor.execute("""
        UPDATE students
        SET balance_due_qar = ?, active_holds = ?
        WHERE student_id = ?;
        """, (rem_due, json.dumps(holds, ensure_ascii=False), student_id))

        conn.commit()
        conn.close()

        return {
            "invoice_number": invoice_number,
            "transaction_reference": txn_ref,
            "amount_paid_qar": amount,
            "payment_status": status,
            "remaining_balance_qar": rem_due,
            "financial_hold_cleared": rem_due <= 0.0
        }
