# -*- coding: utf-8 -*-
"""
Lusail University Domain Engine: Attendance & Absence Rules Engine
Adopted from Frappe Education & RosarioSIS open-source academic standards.
Calculates absence percentage, warnings, and exam exclusion (حرمان).
"""

from typing import Dict, Any

# Lusail University Absence Thresholds
WARNING_1_THRESHOLD_PCT = 10.0   # 10% Absence: First Formal Warning
WARNING_2_THRESHOLD_PCT = 15.0   # 15% Absence: Second Formal Warning
EXCLUSION_THRESHOLD_PCT = 20.0   # 20% Absence: Barred from Final Exam (حرمان أكاديمي)

def evaluate_student_attendance(
    total_lectures: int,
    absent_lectures: int,
    excused_absences: int = 0
) -> Dict[str, Any]:
    """
    Evaluate student absence records and determine academic standing in the course.
    """
    if total_lectures <= 0:
        return {
            'attendance_pct': 100.0,
            'unexcused_absence_pct': 0.0,
            'status': 'منتظم',
            'warning_level': 0,
            'is_barred_from_exam': False,
            'message': 'سجل الحضور مكتمل'
        }

    unexcused_absent = max(0, absent_lectures - excused_absences)
    unexcused_pct = round((unexcused_absent / total_lectures) * 100.0, 1)
    attendance_pct = round(100.0 - unexcused_pct, 1)

    if unexcused_pct >= EXCLUSION_THRESHOLD_PCT:
        return {
            'attendance_pct': attendance_pct,
            'unexcused_absence_pct': unexcused_pct,
            'status': 'حرمان أكاديمي (Barred)',
            'warning_level': 3,
            'is_barred_from_exam': True,
            'message': f'تجاوز نسبة الغياب المسموح بها ({unexcused_pct}%). الطالب محروم من دخول الاختبار النهائي.'
        }
    elif unexcused_pct >= WARNING_2_THRESHOLD_PCT:
        return {
            'attendance_pct': attendance_pct,
            'unexcused_absence_pct': unexcused_pct,
            'status': 'إنذار غياب ثانٍ',
            'warning_level': 2,
            'is_barred_from_exam': False,
            'message': f'إنذار غياب نهائي: نسبة الغياب بلغت {unexcused_pct}% (الحد الأقصى 20%).'
        }
    elif unexcused_pct >= WARNING_1_THRESHOLD_PCT:
        return {
            'attendance_pct': attendance_pct,
            'unexcused_absence_pct': unexcused_pct,
            'status': 'إنذار غياب أول',
            'warning_level': 1,
            'is_barred_from_exam': False,
            'message': f'تنبيه غياب: نسبة الغياب بلغت {unexcused_pct}%.'
        }
    else:
        return {
            'attendance_pct': attendance_pct,
            'unexcused_absence_pct': unexcused_pct,
            'status': 'منتظم',
            'warning_level': 0,
            'is_barred_from_exam': False,
            'message': 'سجل الحضور سليم ومنتظم.'
        }
