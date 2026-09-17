"""
Lusail University Clean Domain Core: Holds & Administrative Rules Engine
Handles Financial, Academic, and Disciplinary Holds enforcement and release.
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime

class StudentHold:
    FINANCIAL = 'Financial'
    ACADEMIC = 'Academic'
    REGISTRAR = 'Registrar'
    DISCIPLINARY = 'Disciplinary'
    NONE = 'None'

def check_can_register(holds: List[str]) -> Tuple[bool, Optional[str]]:
    """
    Returns (True, None) if the student can register for classes,
    or (False, Reason) if blocked by an active hold rule.
    """
    if not holds or holds == [StudentHold.NONE]:
        return True, None

    if StudentHold.FINANCIAL in holds:
        return False, "لا يمكن التسجيل لوجود مستحقات مالية غير مسددة. يرجى سداد الرسوم عبر بوابة QPay."

    if StudentHold.ACADEMIC in holds:
        return False, "لا يمكن التسجيل لوجود إنذار أكاديمي حرج. يرجى مراجعة المرشد الأكاديمي أولاً."

    if StudentHold.DISCIPLINARY in holds:
        return False, "الحساب موقوف إدارياً بقرار من عمادة شؤون الطلاب."

    return False, f"توجد قيود أكاديمية نشطة: {', '.join(holds)}"

def apply_financial_hold_if_balance_due(outstanding_balance: float) -> str:
    """Trigger financial hold if student has outstanding debt > 0 QAR."""
    if outstanding_balance > 0.0:
        return StudentHold.FINANCIAL
    return StudentHold.NONE
