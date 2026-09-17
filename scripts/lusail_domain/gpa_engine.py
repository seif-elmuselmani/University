"""
Lusail University Clean Domain Core: GPA & Academic Standing Engine
Standard 4.00 Scale Calculator following international and regional university standards.
"""

from typing import List, Dict, Tuple, Optional

# Lusail University 4.00 Academic Grading Scale
GRADE_POINTS_TABLE: List[Tuple[float, str, float]] = [
    (95.0, 'A+', 4.00),
    (90.0, 'A',  3.75),
    (85.0, 'B+', 3.50),
    (80.0, 'B',  3.00),
    (75.0, 'C+', 2.75),
    (70.0, 'C',  2.50),
    (65.0, 'D+', 2.25),
    (60.0, 'D',  2.00),
    (0.0,  'F',  0.00),
]

def score_to_grade_and_points(score: float) -> Tuple[str, float]:
    """Convert numerical course score (0-100) to Letter Grade and Grade Points."""
    clamped_score = max(0.0, min(100.0, float(score)))
    for min_score, letter, points in GRADE_POINTS_TABLE:
        if clamped_score >= min_score:
            return letter, points
    return 'F', 0.00

def calculate_gpa(courses: List[Dict]) -> Tuple[float, int, int]:
    """
    Calculate Cumulative GPA, Total Registered Credits, and Total Earned Credits.
    Each course dict expects: {'credits': int, 'score': float} or {'credits': int, 'points': float}
    """
    if not courses:
        return 0.00, 0, 0

    total_quality_points = 0.0
    total_registered_credits = 0
    total_earned_credits = 0

    for c in courses:
        credits = int(c.get('credits', 3))
        total_registered_credits += credits

        if 'score' in c:
            _, points = score_to_grade_and_points(c['score'])
        else:
            points = float(c.get('points', 0.0))

        if points >= 2.00:  # Passing grade at Lusail University (D or higher)
            total_earned_credits += credits

        total_quality_points += (points * credits)

    if total_registered_credits == 0:
        return 0.00, 0, 0

    gpa = round(total_quality_points / total_registered_credits, 2)
    return gpa, total_registered_credits, total_earned_credits

def evaluate_academic_standing(gpa: float, total_credits: int) -> Dict[str, any]:
    """Evaluate student standing (Regular, Honor List, Academic Warning)."""
    if gpa >= 3.75 and total_credits >= 30:
        return {'status': 'منتظم', 'standing': 'Honor Roll (لوحة الشرف)', 'warning_level': 0, 'honor': True}
    elif gpa >= 2.00:
        return {'status': 'منتظم', 'standing': 'Good Standing (وضع أكاديمي سليم)', 'warning_level': 0, 'honor': False}
    elif gpa >= 1.75:
        return {'status': 'تحت الملاحظة', 'standing': 'Academic Warning 1 (إنذار أكاديمي أول)', 'warning_level': 1, 'honor': False}
    else:
        return {'status': 'إنذار أكاديمي', 'standing': 'Critical Academic Warning (إنذار أكاديمي حرج)', 'warning_level': 2, 'honor': False}
