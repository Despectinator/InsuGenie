from .models import DiabetesReport
from .risk import RiskEvaluator
from .recommendations import RecommendationEngine


class DiabetesEngine:
    """
    Main diabetes decision engine.

    Coordinates risk evaluation and recommendation
    generation to produce a final diabetes report.
    """

    def evaluate(self, health_data):

        # Evaluate patient's physiological data
        risk, score, status, alerts = RiskEvaluator.evaluate(
            health_data
        )

        # Generate recommendations
        recommendations = RecommendationEngine.generate(
            alerts
        )

        # Create structured report
        report = DiabetesReport(
            risk_level=risk,
            score=score,
            status=status,
            alerts=alerts,
            recommendations=recommendations,
        )

        return report