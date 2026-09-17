# -*- coding: utf-8 -*-
"""
Enrollment & Grade Recording Repository
Connects grade submission with pure domain GPA calculation and database persistence.
"""

import sys
import os
from typing import List, Dict, Optional, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from scripts.lusail_domain.gpa_engine import calculate_gpa, evaluate_academic_standing, score_to_grade_and_points
from ..database import get_db_connection
from .student_repository import StudentRepository

class EnrollmentRepository:

    @staticmethod
    def get_student_enrollments(student_id: str) -> List[Dict[str, Any]]:
        """Retrieve all course enrollments and grades for a student."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT e.id, e.student_id, e.course_code, c.title_ar, c.title_en, c.credits, e.semester, e.score, e.letter_grade, e.grade_points, e.status
        FROM enrollments e
        JOIN courses c ON e.course_code = c.course_code
        WHERE e.student_id = ?
        ORDER BY e.semester, e.course_code;
        """, (student_id,))
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def record_or_update_grade(student_id: str, course_code: str, semester: str, score: float) -> Dict[str, Any]:
        """
        Record or update a student's course grade, determine letter grade/points, 
        and automatically recalculate and persist student's cumulative GPA.
        """
        letter_grade, grade_points = score_to_grade_and_points(score)
        status = 'ناجح' if grade_points >= 2.0 else 'راسب'

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if enrollment already exists
        cursor.execute("""
        SELECT id FROM enrollments 
        WHERE student_id = ? AND course_code = ? AND semester = ?;
        """, (student_id, course_code, semester))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
            UPDATE enrollments
            SET score = ?, letter_grade = ?, grade_points = ?, status = ?
            WHERE id = ?;
            """, (score, letter_grade, grade_points, status, existing['id']))
        else:
            cursor.execute("""
            INSERT INTO enrollments (student_id, course_code, semester, score, letter_grade, grade_points, status)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (student_id, course_code, semester, score, letter_grade, grade_points, status))

        conn.commit()

        # Recalculate Student GPA from all courses
        cursor.execute("""
        SELECT c.credits, e.score
        FROM enrollments e
        JOIN courses c ON e.course_code = c.course_code
        WHERE e.student_id = ? AND e.score IS NOT NULL;
        """, (student_id,))
        course_data = [dict(r) for r in cursor.fetchall()]
        conn.close()

        new_gpa, reg_credits, earned_credits = calculate_gpa(course_data)
        standing_info = evaluate_academic_standing(new_gpa, earned_credits)

        # Persist new GPA in students table
        StudentRepository.update_academic_summary(
            student_id=student_id,
            gpa=new_gpa,
            earned_credits=earned_credits,
            registered_credits=reg_credits,
            standing=standing_info['standing']
        )

        return {
            "student_id": student_id,
            "course_code": course_code,
            "score": score,
            "letter_grade": letter_grade,
            "grade_points": grade_points,
            "status": status,
            "new_cumulative_gpa": new_gpa,
            "total_earned_credits": earned_credits,
            "academic_standing": standing_info['standing']
        }
