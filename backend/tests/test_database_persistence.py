# -*- coding: utf-8 -*-
"""
End-to-End Database Persistence & Clean Architecture Test Suite
Verifies data integrity, repository operations, and real-time state persistence in SQLite.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.database import init_db, get_db_connection
from backend.repositories.student_repository import StudentRepository
from backend.repositories.enrollment_repository import EnrollmentRepository
from backend.repositories.admission_repository import AdmissionRepository
from backend.repositories.service_ticket_repository import ServiceTicketRepository
from backend.repositories.finance_repository import FinanceRepository

class TestDatabasePersistence(unittest.TestCase):

    def setUp(self):
        """Re-seed clean dataset before each test to guarantee test isolation."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS enrollments;")
        cursor.execute("DROP TABLE IF EXISTS invoices;")
        cursor.execute("DROP TABLE IF EXISTS service_tickets;")
        cursor.execute("DROP TABLE IF EXISTS admission_applications;")
        cursor.execute("DROP TABLE IF EXISTS students;")
        cursor.execute("DROP TABLE IF EXISTS courses;")
        cursor.execute("DROP TABLE IF EXISTS users;")
        conn.commit()
        conn.close()
        init_db()

    def test_01_student_repository_read(self):
        """Test reading students and active holds from SQLite."""
        students = StudentRepository.get_all()
        self.assertGreater(len(students), 0)
        maryam = next((s for s in students if s['student_id'] == 'LU-2024-0891'), None)
        self.assertIsNotNone(maryam)
        self.assertEqual(maryam['college'], 'كلية تكنولوجيا المعلومات')
        self.assertIsInstance(maryam['active_holds'], list)

    def test_02_grade_recording_and_gpa_recalculation(self):
        """Test recording a grade, automatic GPA update, and verification across connection restarts."""
        student_id = "LU-2024-0891"
        
        # Record a 100% score for a course
        result = EnrollmentRepository.record_or_update_grade(
            student_id=student_id,
            course_code="AI301",
            semester="خريف 2026",
            score=100.0
        )
        self.assertEqual(result['letter_grade'], 'A+')
        self.assertEqual(result['grade_points'], 4.0)

        # Close and Re-open DB Connection to assert disk persistence
        reloaded_student = StudentRepository.get_by_id(student_id)
        self.assertIsNotNone(reloaded_student)
        self.assertGreaterEqual(reloaded_student['gpa'], 3.75)
        self.assertTrue(
            "Good Standing" in reloaded_student['academic_standing'] or 
            "Honor" in reloaded_student['academic_standing']
        )

    def test_03_admission_application_persistence(self):
        """Test submitting admission application and persisting to SQLite."""
        app_data = {
            "full_name": "سلطان بن فهد النعيمي",
            "national_id": "30163407788",
            "nationality": "قطري",
            "email": "sultan.n@example.qa",
            "phone": "+974 5511 2233",
            "first_choice_college": "كلية تكنولوجيا المعلومات",
            "first_choice_major": "بكالوريوس الذكاء الاصطناعي",
            "high_school_gpa": 95.5
        }
        saved = AdmissionRepository.create_application(app_data)
        self.assertTrue(saved['application_id'].startswith("APP-2026-"))
        self.assertEqual(saved['status'], "مقبول مبدئياً")

        # Query all applications to verify presence
        all_apps = AdmissionRepository.get_all()
        found = any(a['application_id'] == saved['application_id'] for a in all_apps)
        self.assertTrue(found)

    def test_04_service_ticket_persistence(self):
        """Test creating service ticket in database."""
        ticket = ServiceTicketRepository.create_ticket(
            student_id="LU-2024-0891",
            service_code="SRV-01",
            service_name="كشف درجات رسمي معتمد",
            details="طلب نسخة ورقية مختومة لتقديمها لجهة الابتعاث"
        )
        self.assertTrue(ticket['ticket_id'].startswith("TCK-SRV-01-"))
        self.assertEqual(ticket['status'], "قيد المعالجة")

        # Verify from DB
        tickets = ServiceTicketRepository.get_by_student("LU-2024-0891")
        self.assertGreater(len(tickets), 0)

    def test_05_finance_payment_and_hold_release(self):
        """Test paying an invoice and verifying automatic release of financial hold."""
        student_id = "LU-2024-0312"
        st_before = StudentRepository.get_by_id(student_id)
        self.assertIn("Financial", st_before['active_holds'])
        
        # Pay the remaining balance (23250 - 18750 = 4500 QAR)
        pay_res = FinanceRepository.process_payment(
            invoice_number="INV-2026-002",
            student_id=student_id,
            amount=4500.0
        )
        self.assertIsNotNone(pay_res)
        self.assertEqual(pay_res['payment_status'], 'مدفوع كلياً')

        # Re-fetch student to verify Financial hold was removed from DB
        st_after = StudentRepository.get_by_id(student_id)
        self.assertEqual(st_after['balance_due_qar'], 0.0)
        self.assertNotIn("Financial", st_after['active_holds'])

if __name__ == "__main__":
    unittest.main()
