# -*- coding: utf-8 -*-
"""
Lusail University Domain Engine: Prerequisites & Registration Validator
Inspired by UniTime and Frappe Education registration rule engines.
Ensures student passed prerequisite courses before enrolling in advanced courses.
"""

from typing import List, Dict, Tuple, Optional

def validate_course_registration(
    course_to_register: str,
    required_prerequisites: List[str],
    passed_courses: List[str]
) -> Tuple[bool, Optional[str]]:
    """
    Validate whether a student is eligible to register for a course.
    Returns (True, None) if eligible, or (False, error_reason) if prerequisites are missing.
    """
    if not required_prerequisites:
        return True, None

    missing = [req for req in required_prerequisites if req not in passed_courses]
    if missing:
        missing_str = ", ".join(missing)
        return False, f"لا يمكن تسجيل المقرر {course_to_register} قبل اجتياز المتطلب السابق: ({missing_str})"

    return True, None

def check_schedule_conflict(
    new_slot: Dict[str, str],
    enrolled_slots: List[Dict[str, str]]
) -> Tuple[bool, Optional[str]]:
    """
    Check if a course lecture time conflicts with already enrolled courses.
    Each slot dict: {'days': 'UT' (Sun/Tue) or 'MW' (Mon/Wed), 'start_time': '09:00', 'end_time': '10:15', 'course_code': 'IT101'}
    """
    new_days = set(new_slot.get('days', ''))
    new_start = new_slot.get('start_time', '')
    new_end = new_slot.get('end_time', '')

    for slot in enrolled_slots:
        slot_days = set(slot.get('days', ''))
        # If they share at least one day
        if new_days.intersection(slot_days):
            # Check time overlap
            if not (new_end <= slot.get('start_time', '') or new_start >= slot.get('end_time', '')):
                return False, f"تعارض في الجدول الدراسي مع مقرر {slot.get('course_code', 'سابق')} في التوقيت ({slot.get('start_time')}-{slot.get('end_time')})"

    return True, None
