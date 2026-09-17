# -*- coding: utf-8 -*-
"""
Student Repository - Data access layer for Students and Academic Profiles
"""

import json
from typing import List, Dict, Optional, Any
from ..database import get_db_connection

class StudentRepository:
    
    @staticmethod
    def get_all() -> List[Dict[str, Any]]:
        """Fetch all students with parsed holds."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT student_id, user_id, full_name, college, major, gpa, earned_credits, registered_credits, academic_standing, active_holds, balance_due_qar, scholarship_type
        FROM students
        ORDER BY student_id ASC;
        """)
        rows = cursor.fetchall()
        conn.close()

        students = []
        for r in rows:
            st = dict(r)
            st['active_holds'] = json.loads(st['active_holds']) if st['active_holds'] else []
            students.append(st)
        return students

    @staticmethod
    def get_by_id(student_id: str) -> Optional[Dict[str, Any]]:
        """Fetch a single student by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?;", (student_id,))
        row = cursor.fetchone()
        conn.close()
        if not row:
            return None
        st = dict(row)
        st['active_holds'] = json.loads(st['active_holds']) if st['active_holds'] else []
        return st

    @staticmethod
    def update_academic_summary(student_id: str, gpa: float, earned_credits: int, registered_credits: int, standing: str):
        """Persist recalculated GPA and standing into database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE students
        SET gpa = ?, earned_credits = ?, registered_credits = ?, academic_standing = ?
        WHERE student_id = ?;
        """, (gpa, earned_credits, registered_credits, standing, student_id))
        conn.commit()
        conn.close()
