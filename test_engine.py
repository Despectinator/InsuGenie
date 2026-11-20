from app.diabetes.models import HealthData
from app.diabetes.engine import DiabetesEngine

engine = DiabetesEngine()

sample = HealthData(
    heart_rate=115,
    blood_glucose=280,
    spo2=90,
    systolic_bp=150,
    diastolic_bp=95,
    body_temperature=38.7,
    hrv=18,
)

report = engine.evaluate(sample)

print("Risk:", report.risk_level)
print("Score:", report.score)
print("Status:", report.status)

print("\nAlerts:")
for alert in report.alerts:
    print("-", alert)

print("\nRecommendations:")
for recommendation in report.recommendations:
    print("-", recommendation)