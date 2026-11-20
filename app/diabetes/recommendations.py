class RecommendationEngine:
    """
    Generates patient recommendations based on
    detected medical alerts.
    """

    @staticmethod
    def generate(alerts):

        recommendations = []

        # -------------------------
        # Heart Rate
        # -------------------------

        if "Elevated Heart Rate" in alerts:
            recommendations.append(
                "Sit down and rest for 10 minutes."
            )
            recommendations.append(
                "Drink water."
            )
            recommendations.append(
                "Recheck your heart rate."
            )

        if "Bradycardia" in alerts:
            recommendations.append(
                "Consult a healthcare provider."
            )

        # -------------------------
        # Blood Glucose
        # -------------------------

        if "High Blood Glucose" in alerts:
            recommendations.append(
                "Monitor blood glucose closely."
            )
            recommendations.append(
                "Follow your prescribed medication plan."
            )

        if "Severe Hyperglycemia" in alerts:
            recommendations.append(
                "Seek immediate medical advice."
            )

        if "Hypoglycemia" in alerts:
            recommendations.append(
                "Consume 15 g of fast-acting carbohydrates."
            )
            recommendations.append(
                "Recheck blood glucose after 15 minutes."
            )

        # -------------------------
        # Oxygen Saturation
        # -------------------------

        if "Low Oxygen Saturation" in alerts:
            recommendations.append(
                "Seek emergency medical care if symptoms persist."
            )

        # -------------------------
        # Blood Pressure
        # -------------------------

        if "High Blood Pressure" in alerts:
            recommendations.append(
                "Reduce physical activity and monitor blood pressure."
            )
            recommendations.append(
                "Contact your healthcare provider if it remains elevated."
            )

        if "Hypertensive Crisis" in alerts:
            recommendations.append(
                "Seek emergency medical attention immediately."
            )

        # -------------------------
        # Body Temperature
        # -------------------------

        if "Fever" in alerts:
            recommendations.append(
                "Stay hydrated and monitor your temperature."
            )

        if "Hypothermia" in alerts:
            recommendations.append(
                "Warm the body gradually and seek medical attention."
            )

        # -------------------------
        # HRV
        # -------------------------

        if "Low HRV" in alerts:
            recommendations.append(
                "Reduce stress and allow adequate recovery."
            )

        # -------------------------
        # No Alerts
        # -------------------------

        if not recommendations:
            recommendations.append(
                "Continue maintaining a healthy lifestyle."
            )

        return recommendations