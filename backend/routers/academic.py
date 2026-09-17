# -*- coding: utf-8 -*-
"""
Academic Records, Transcripts, Attendance & Prerequisite Validation Router
Combines StudentRepository, EnrollmentRepository, and domain engines.
"""

import sys
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from scripts.lusail_domain.attendance_engine import evaluate_student_attendance
from scripts.lusail_domain.prerequisite_engine import validate_course_registration, check_schedule_conflict
from ..repositories.student_repository import StudentRepository
from ..repositories.enrollment_repository import EnrollmentRepository
from ..database import get_db_connection

router = APIRouter(prefix="/api/academic", tags=["Academic & Transcripts"])

class RecordGradeRequest(BaseModel):
    student_id: str
    course_code: str
    semester: str = "خريف 2026"
    score: float

class AttendanceEvaluationRequest(BaseModel):
    total_lectures: int = 30
    absent_lectures: int
    excused_absences: int = 0

class ValidateRegistrationRequest(BaseModel):
    student_id: str
    course_to_register: str
    required_prerequisites: List[str] = []

@router.get("/students")
def list_students():
    """Retrieve all students currently stored in SQLite database."""
    students = StudentRepository.get_all()
    return {"status": "success", "count": len(students), "students": students}

@router.get("/courses")
def list_courses():
    """Retrieve all university courses organized by college."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses ORDER BY college, course_code;")
    courses = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"status": "success", "count": len(courses), "courses": courses}

@router.get("/students/{student_id}/transcript")
def get_student_transcript(student_id: str):
    """Retrieve full official transcript with real-time GPA from database."""
    student = StudentRepository.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="رقم الطالب غير موجود في السجل الأكاديمي")

    enrollments = EnrollmentRepository.get_student_enrollments(student_id)

    return {
        "status": "success",
        "student": student,
        "academic_summary": {
            "cumulative_gpa": student["gpa"],
            "total_registered_credits": student["registered_credits"],
            "total_earned_credits": student["earned_credits"],
            "academic_standing": student["academic_standing"],
            "is_honor_roll": student["gpa"] >= 3.75
        },
        "courses_history": enrollments
    }

@router.post("/grades/record")
def record_course_grade(req: RecordGradeRequest):
    """
    Record or update a student's course grade.
    Saves to SQLite and immediately recalculates and updates the student's cumulative GPA.
    """
    student = StudentRepository.get_by_id(req.student_id)
    if not student:
        raise HTTPException(status_code=404, detail="رقم الطالب غير موجود")

    if req.score < 0 or req.score > 100:
        raise HTTPException(status_code=400, detail="الدرجة يجب أن تكون بين 0 و 100")

    result = EnrollmentRepository.record_or_update_grade(
        student_id=req.student_id,
        course_code=req.course_code,
        semester=req.semester,
        score=req.score
    )

    return {
        "status": "success",
        "message": f"تم رصد الدرجة ({req.score}%) للمقرر {req.course_code} بنجاح، وتحديث المعدل التراكمي في قاعدة البيانات فورياً.",
        "record": result
    }

@router.post("/attendance/evaluate")
def evaluate_attendance(req: AttendanceEvaluationRequest):
    """Calculate absence percentage and warning thresholds (10%, 15%, 20% حرمان)."""
    result = evaluate_student_attendance(
        total_lectures=req.total_lectures,
        absent_lectures=req.absent_lectures,
        excused_absences=req.excused_absences
    )
    return {"status": "success", "evaluation": result}

@router.post("/registration/validate")
def validate_registration(req: ValidateRegistrationRequest):
    """Check prerequisites compliance based on student passed courses in database."""
    enrollments = EnrollmentRepository.get_student_enrollments(req.student_id)
    passed_courses = [e['course_code'] for e in enrollments if e['grade_points'] and e['grade_points'] >= 2.0]

    can_register, reason = validate_course_registration(
        course_to_register=req.course_to_register,
        required_prerequisites=req.required_prerequisites,
        passed_courses=passed_courses
    )

    if not can_register:
        raise HTTPException(status_code=400, detail=reason)

    return {
        "status": "success",
        "can_register": True,
        "message": f"تم استيفاء كافة المتطلبات السابقة للمقرر {req.course_to_register} بنجاح."
    }
