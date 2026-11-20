from .models import HealthData


class RiskEvaluator:
    """
    Evaluates physiological measurements and
    determines the patient's diabetes-related risk.
    """

    @staticmethod
    def evaluate(data: HealthData):

        score = 0
        alerts = []
        status = "Stable"

        # -------------------------
        # Heart Rate
        # -------------------------

        if data.heart_rate is not None:

            if data.heart_rate < 50:
                score += 40
                alerts.append("Bradycardia")

            elif data.heart_rate > 100:
                score += 30
                alerts.append("Elevated Heart Rate")

        # -------------------------
        # Blood Glucose
        # -------------------------

        if data.blood_glucose is not None:

            if data.blood_glucose > 250:
                score += 60
                alerts.append("Severe Hyperglycemia")

            elif data.blood_glucose > 180:
                score += 40
                alerts.append("High Blood Glucose")

            elif data.blood_glucose < 70:
                score += 70
                alerts.append("Hypoglycemia")

        # -------------------------
        # Oxygen Saturation
        # -------------------------

        if data.spo2 is not None:

            if data.spo2 < 92:
                score += 50
                alerts.append("Low Oxygen Saturation")

        # -------------------------
        # Blood Pressure
        # -------------------------

        if (
            data.systolic_bp is not None
            and data.diastolic_bp is not None
        ):

            if data.systolic_bp >= 180 or data.diastolic_bp >= 120:
                score += 60
                alerts.append("Hypertensive Crisis")

            elif data.systolic_bp >= 140 or data.diastolic_bp >= 90:
                score += 30
                alerts.append("High Blood Pressure")

        # -------------------------
        # Body Temperature
        # -------------------------

        if data.body_temperature is not None:

            if data.body_temperature >= 38.5:
                score += 20
                alerts.append("Fever")

            elif data.body_temperature < 35:
                score += 30
                alerts.append("Hypothermia")

        # -------------------------
        # Heart Rate Variability
        # -------------------------

        if data.hrv is not None:

            if data.hrv < 20:
                score += 15
                alerts.append("Low HRV")

        # -------------------------
        # Risk Classification
        # -------------------------

        if score < 20:
            risk = "Low"

        elif score < 50:
            risk = "Moderate"

        elif score < 80:
            risk = "High"

        else:
            risk = "Critical"

        if alerts:
            status = "Attention Required"

        return risk, score, status, alerts