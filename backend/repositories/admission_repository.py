# -*- coding: utf-8 -*-
"""
Admissions Repository - Data access layer for student applications
"""

from datetime import datetime
from typing import List, Dict, Optional, Any
from ..database import get_db_connection

class AdmissionRepository:

    @staticmethod
    def create_application(data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a new admission application to database."""
        app_id = f"APP-2026-{int(datetime.now().timestamp()) % 100000:05d}"
        high_school_gpa = float(data.get('high_school_gpa', 80.0))
        status = "مقبول مبدئياً" if high_school_gpa >= 75.0 else "قيد المراجعة"

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO admission_applications 
        (application_id, full_name, national_id, nationality, email, phone, first_choice_college, first_choice_major, high_school_gpa, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            app_id,
            data['full_name'],
            data['national_id'],
            data.get('nationality', 'قطري'),
            data['email'],
            data['phone'],
            data['first_choice_college'],
            data['first_choice_major'],
            high_school_gpa,
            status
        ))
        conn.commit()
        conn.close()

        return {
            "application_id": app_id,
            "full_name": data['full_name'],
            "college": data['first_choice_college'],
            "major": data['first_choice_major'],
            "high_school_gpa": high_school_gpa,
            "status": status,
            "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def get_all() -> List[Dict[str, Any]]:
        """List all admission applications ordered by submission date."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admission_applications ORDER BY submitted_at DESC;")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def update_status(application_id: str, new_status: str) -> bool:
        """Update admission status (e.g. مقبول نهائياً / مرفوض)."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE admission_applications SET status = ? WHERE application_id = ?;", (new_status, application_id))
        conn.commit()
        affected = cursor.rowcount > 0
        conn.close()
        return affected
