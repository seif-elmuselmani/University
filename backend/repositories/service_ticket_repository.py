# -*- coding: utf-8 -*-
"""
Service Ticket Repository - Data access layer for student service requests
"""

from datetime import datetime
from typing import List, Dict, Optional, Any
from ..database import get_db_connection

class ServiceTicketRepository:

    @staticmethod
    def create_ticket(student_id: str, service_code: str, service_name: str, details: str = "") -> Dict[str, Any]:
        """Create and store a service ticket in database."""
        ticket_id = f"TCK-{service_code}-{int(datetime.now().timestamp()) % 100000:05d}"
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO service_tickets (ticket_id, student_id, service_code, service_name, details, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, 'قيد المعالجة', ?, ?);
        """, (ticket_id, student_id, service_code, service_name, details, now_str, now_str))
        conn.commit()
        conn.close()

        return {
            "ticket_id": ticket_id,
            "student_id": student_id,
            "service_code": service_code,
            "service_name": service_name,
            "details": details,
            "status": "قيد المعالجة",
            "created_at": now_str
        }

    @staticmethod
    def get_all() -> List[Dict[str, Any]]:
        """List all service tickets."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT t.*, s.full_name as student_name, s.college
        FROM service_tickets t
        LEFT JOIN students s ON t.student_id = s.student_id
        ORDER BY t.created_at DESC;
        """)
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def get_by_student(student_id: str) -> List[Dict[str, Any]]:
        """List tickets for a specific student."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM service_tickets WHERE student_id = ? ORDER BY created_at DESC;", (student_id,))
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows
