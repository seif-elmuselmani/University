"""
Lusail University Clean Domain Core: Tuition Fee & Scholarships Calculator
Calculates Credit Hour Fees in Qatari Riyals (QAR), discounts, and net payable.
"""

from typing import Dict, Optional

# Lusail University Standard Rate: 1,500 QAR per Credit Hour
CREDIT_HOUR_RATE_QAR = 1500.0
ADMISSION_APPLICATION_FEE_QAR = 500.0
STUDENT_SERVICES_FEE_SEMESTER_QAR = 750.0

SCHOLARSHIP_DISCOUNTS = {
    'NONE': 0.0,
    'ACADEMIC_EXCELLENCE_50': 0.50,   # 50% Merit Discount for GPA >= 3.90
    'FULL_SPONSORSHIP_100': 1.00,     # 100% Full Ministry/University Scholarship
    'SIBLING_DISCOUNT_15': 0.15,      # 15% Sibling Discount
}

def calculate_semester_tuition(
    credits: int,
    scholarship_type: str = 'NONE',
    include_services_fee: bool = True
) -> Dict[str, any]:
    """
    Calculate full semester tuition breakdown in Qatari Riyals (QAR).
    """
    base_tuition = float(credits) * CREDIT_HOUR_RATE_QAR
    discount_pct = SCHOLARSHIP_DISCOUNTS.get(scholarship_type, 0.0)
    discount_amount = base_tuition * discount_pct
    net_tuition = base_tuition - discount_amount

    services_fee = STUDENT_SERVICES_FEE_SEMESTER_QAR if include_services_fee else 0.0
    total_payable = net_tuition + services_fee

    return {
        'credits': credits,
        'rate_per_credit_qar': CREDIT_HOUR_RATE_QAR,
        'base_tuition_qar': base_tuition,
        'scholarship_type': scholarship_type,
        'discount_percentage': int(discount_pct * 100),
        'discount_amount_qar': discount_amount,
        'services_fee_qar': services_fee,
        'total_payable_qar': total_payable,
        'currency': 'ر.ق (QAR)'
    }
