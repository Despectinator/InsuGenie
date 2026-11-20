from .patient import Patient
from .models import HealthData


class GlucoseEstimator:
    """
    AI-inspired glucose estimator for research/demo purposes.

    IMPORTANT:
    This does NOT directly measure blood glucose.
    It estimates glucose using physiological measurements
    and patient characteristics.
    """

    @staticmethod
    def estimate(patient: Patient, health: HealthData):

        bmi = patient.weight_kg / ((patient.height_cm / 100) ** 2)

        glucose = 90.0

        # ----------------------------
        # Age
        # ----------------------------

        if patient.age > 45:
            glucose += 8

        elif patient.age > 35:
            glucose += 4

        # ----------------------------
        # BMI
        # ----------------------------

        if bmi > 30:
            glucose += 18

        elif bmi > 25:
            glucose += 10

        # ----------------------------
        # Heart Rate
        # ----------------------------

        if health.heart_rate is not None:

            if health.heart_rate > 100:
                glucose += 12

            elif health.heart_rate > 90:
                glucose += 6

        # ----------------------------
        # HRV
        # ----------------------------

        if health.hrv is not None:

            if health.hrv < 25:
                glucose += 8

        # ----------------------------
        # Hypertension
        # ----------------------------

        if patient.hypertension:
            glucose += 10

        # ----------------------------
        # Smoker
        # ----------------------------

        if patient.smoker:
            glucose += 5

        glucose = max(70, min(glucose, 280))

        return round(glucose, 1)