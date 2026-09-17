# -*- coding: utf-8 -*-
"""
Financial & Bursar Services Router
Leverages FinanceRepository and pure domain calculation.
"""

import sys
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from scripts.lusail_domain.fee_calculator import calculate_semester_tuition
from ..repositories.finance_repository import FinanceRepository

router = APIRouter(prefix="/api/finance", tags=["Finance & Tuition"])

class TuitionCalculationRequest(BaseModel):
    credits: int = 15
    scholarship_type: str = "NONE"
    include_services_fee: bool = True

class PayInvoiceRequest(BaseModel):
    invoice_number: str
    student_id: str
    amount: float
    payment_method: str = "QPAY_DEBIT_CARD"

@router.get("/invoices")
def list_invoices():
    """Retrieve all student invoices stored in SQLite."""
    invoices = FinanceRepository.get_all_invoices()
    return {"status": "success", "count": len(invoices), "invoices": invoices}

@router.post("/calculate-tuition")
def calculate_tuition_breakdown(req: TuitionCalculationRequest):
    """Dynamic tuition calculation using Lusail University domain engine."""
    if req.credits < 1 or req.credits > 24:
        raise HTTPException(status_code=400, detail="عدد الساعات يجب أن يكون بين 1 و 24 ساعة معتمدة.")
    
    breakdown = calculate_semester_tuition(
        credits=req.credits,
        scholarship_type=req.scholarship_type,
        include_services_fee=req.include_services_fee
    )
    return {"status": "success", "breakdown": breakdown}

@router.get("/students/{student_id}/ledger")
def get_student_financial_ledger(student_id: str):
    """Retrieve full student financial statement and invoice breakdown from database."""
    ledger = FinanceRepository.get_student_ledger(student_id)
    if not ledger:
        raise HTTPException(status_code=404, detail="الطالب غير مسجل في السجلات المالية")
    return {"status": "success", **ledger}

@router.post("/pay-invoice")
def pay_invoice(req: PayInvoiceRequest):
    """Process an invoice payment, record transaction, and release financial hold if fully settled."""
    result = FinanceRepository.process_payment(
        invoice_number=req.invoice_number,
        student_id=req.student_id,
        amount=req.amount
    )
    if not result:
        raise HTTPException(status_code=404, detail="رقم الفاتورة غير صحيح أو لا يخص هذا الطالب")

    return {
        "status": "success",
        "message": "تم سداد الفاتورة بنجاح وتحديث السجل المالي فورياً في قاعدة البيانات",
        **result
    }
