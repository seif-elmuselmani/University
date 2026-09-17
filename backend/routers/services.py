# -*- coding: utf-8 -*-
"""
E-Services Hub & Student Service Tickets Router
Leverages ServiceTicketRepository for database persistence.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
from ..repositories.service_ticket_repository import ServiceTicketRepository
from ..repositories.student_repository import StudentRepository

router = APIRouter(prefix="/api/services", tags=["E-Services"])

# 16 Comprehensive Services Catalog
SERVICES_CATALOG = [
    {"code": "SRV-01", "name": "كشف درجات رسمي معتمد", "category": "أكاديمية", "fee_qar": 50.0, "processing_time": "فوري"},
    {"code": "SRV-02", "name": "إثبات قيد طالب منتظم", "category": "أكاديمية", "fee_qar": 0.0, "processing_time": "فوري"},
    {"code": "SRV-03", "name": "طلب تأجيل فصل دراسي", "category": "تسجيل", "fee_qar": 0.0, "processing_time": "يوم عمل"},
    {"code": "SRV-04", "name": "طلب تحويل بين الكليات", "category": "تسجيل", "fee_qar": 100.0, "processing_time": "3 أيام عمل"},
    {"code": "SRV-05", "name": "طلب سحب وإضافة مقرر بعد الموعد", "category": "أكاديمية", "fee_qar": 50.0, "processing_time": "يوم عمل"},
    {"code": "SRV-06", "name": "سداد الرسوم الدراسية (QPay)", "category": "مالية", "fee_qar": 0.0, "processing_time": "فوري"},
    {"code": "SRV-07", "name": "طلب تقسيط الرسوم الدراسية", "category": "مالية", "fee_qar": 0.0, "processing_time": "يومان"},
    {"code": "SRV-08", "name": "طلب منحة التفوق الأكاديمي (50%)", "category": "مالية", "fee_qar": 0.0, "processing_time": "5 أيام"},
    {"code": "SRV-09", "name": "طلب بطاقة جامعية بديلة", "category": "خدمات عامة", "fee_qar": 50.0, "processing_time": "يوم عمل"},
    {"code": "SRV-10", "name": "حجز موعد إرشاد أكاديمي", "category": "أكاديمية", "fee_qar": 0.0, "processing_time": "فوري"},
    {"code": "SRV-11", "name": "طلب تصريح مواقف الحرم الجامعي", "category": "خدمات عامة", "fee_qar": 0.0, "processing_time": "يوم عمل"},
    {"code": "SRV-12", "name": "طلب إعارة مصادر ومراجع المكتبة", "category": "مكتبية", "fee_qar": 0.0, "processing_time": "فوري"},
    {"code": "SRV-13", "name": "طلب معادلة مساقات سابقة", "category": "تسجيل", "fee_qar": 200.0, "processing_time": "5 أيام"},
    {"code": "SRV-14", "name": "تسجيل الأنشطة والأندية الطلابية", "category": "شؤون طلاب", "fee_qar": 0.0, "processing_time": "فوري"},
    {"code": "SRV-15", "name": "طلب شهادة حسن سيرة وسلوك", "category": "شؤون طلاب", "fee_qar": 0.0, "processing_time": "يوم عمل"},
    {"code": "SRV-16", "name": "طلب فحص تظلم على درجة نهائية", "category": "أكاديمية", "fee_qar": 100.0, "processing_time": "3 أيام"}
]

class SubmitServiceTicketRequest(BaseModel):
    student_id: str
    service_code: str
    details: Optional[str] = None

@router.get("/catalog")
def get_services_catalog():
    """Retrieve the full 16 e-services catalog."""
    return {"status": "success", "count": len(SERVICES_CATALOG), "services": SERVICES_CATALOG}

@router.get("/tickets")
def list_all_service_tickets():
    """Retrieve all service tickets stored in SQLite database."""
    tickets = ServiceTicketRepository.get_all()
    return {"status": "success", "count": len(tickets), "tickets": tickets}

@router.post("/submit")
def submit_service_ticket(req: SubmitServiceTicketRequest):
    """Submit a service request ticket and persist in database."""
    srv = next((s for s in SERVICES_CATALOG if s["code"] == req.service_code), None)
    if not srv:
        raise HTTPException(status_code=404, detail="رمز الخدمة غير صحيح")

    student = StudentRepository.get_by_id(req.student_id)
    if not student:
        raise HTTPException(status_code=404, detail="رقم الطالب غير مسجل في قاعدة البيانات")

    ticket = ServiceTicketRepository.create_ticket(
        student_id=req.student_id,
        service_code=srv['code'],
        service_name=srv['name'],
        details=req.details or ""
    )

    return {
        "status": "success",
        "message": f"تم استلام طلب ({srv['name']}) بنجاح وتوثيق التذكرة في قاعدة البيانات",
        "ticket": ticket
    }

@router.get("/students/{student_id}/tickets")
def get_student_tickets(student_id: str):
    """List all submitted tickets for a given student."""
    tickets = ServiceTicketRepository.get_by_student(student_id)
    return {"status": "success", "count": len(tickets), "tickets": tickets}
