# -*- coding: utf-8 -*-
"""
Admissions & Enrollment Applications Router
Leverages AdmissionRepository for persistent storage.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from ..repositories.admission_repository import AdmissionRepository

router = APIRouter(prefix="/api/admissions", tags=["Admissions & Enrollment"])

class AdmissionApplicationInput(BaseModel):
    full_name: str
    national_id: str
    nationality: str = "قطري"
    email: str
    phone: str
    first_choice_college: str
    first_choice_major: str
    high_school_gpa: float

class UpdateStatusInput(BaseModel):
    status: str

@router.post("/apply")
def submit_admission_application(req: AdmissionApplicationInput):
    """Submit a new student admission application and persist in SQLite."""
    if req.high_school_gpa < 65.0:
        raise HTTPException(status_code=400, detail="الحد الأدنى لتقديم طلب القبول هو 65% في الثانوية العامة.")

    saved_app = AdmissionRepository.create_application(req.model_dump())

    return {
        "status": "success",
        "message": "تم استلام طلب القبول بنجاح وتسجيله في قاعدة البيانات المركزية",
        "application": saved_app
    }

@router.get("/applications")
def list_admission_applications():
    """Retrieve all admission applications stored in database."""
    apps = AdmissionRepository.get_all()
    return {"status": "success", "count": len(apps), "applications": apps}

@router.patch("/applications/{application_id}/status")
def update_application_status(application_id: str, req: UpdateStatusInput):
    """Update status of an admission application."""
    success = AdmissionRepository.update_status(application_id, req.status)
    if not success:
        raise HTTPException(status_code=404, detail="رقم الطلب غير موجود")
    return {"status": "success", "message": f"تم تحديث حالة الطلب إلى ({req.status}) بنجاح"}
