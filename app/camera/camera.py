from app.diabetes.glucose_estimator import GlucoseEstimator
from app.diabetes.patient import Patient
from app.diabetes.engine import DiabetesEngine
from app.diabetes.models import HealthData

from app.rppg.wrapper import RPPGWrapper
from app.rppg.frame_buffer import FrameBuffer
from app.rppg.roi import ROIExtractor
from .face_detector import FaceDetector

import cv2
import time


class Camera:

    def __init__(self):

        # -----------------------------
        # Diabetes Engine
        # -----------------------------
        self.diabetes_engine = DiabetesEngine()

        # Store latest outputs
        self.latest_report = None
        self.latest_glucose = None

        # -----------------------------
        # Demo Patient
        # -----------------------------
        self.patient = Patient(
            patient_id=1,
            name="Demo User",
            age=23,
            gender="Male",
            height_cm=175,
            weight_kg=72,
            diabetes_type="Unknown",
            smoker=False,
            hypertension=False,
        )

        # -----------------------------
        # Vision Components
        # -----------------------------
        self.face_detector = FaceDetector()
        self.frame_buffer = FrameBuffer(max_frames=300)

        # -----------------------------
        # rPPG Wrapper
        # -----------------------------
        self.wrapper = RPPGWrapper()
        self.wrapper.initialize()
                # -----------------------------
        # Camera
        # -----------------------------
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        # Get camera FPS
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        # Some webcams incorrectly report FPS
        if self.fps <= 1:
            self.fps = 30.0

        print(f"Camera FPS: {self.fps}")

        # Timing
        self.prev_time = 0
        self.last_measurement = 0

        # Latest measurements
        self.heart_rate = "--"

        print("Camera initialized successfully.")

    def start(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                break

            # -----------------------------
            # Face Detection
            # -----------------------------
            frame, bbox = self.face_detector.detect(frame)

            # -----------------------------
            # Forehead ROI
            # -----------------------------
            roi = ROIExtractor.extract_forehead(frame, bbox)

            if roi is not None:
                self.frame_buffer.add(roi)

            # -----------------------------
            # Draw ROI
            # -----------------------------
            if bbox is not None:

                x, y, w, h = bbox

                fx = x + int(w * 0.25)
                fy = y + int(h * 0.10)

                fw = int(w * 0.50)
                fh = int(h * 0.20)

                cv2.rectangle(
                    frame,
                    (fx, fy),
                    (fx + fw, fy + fh),
                    (255, 0, 0),
                    2,
                )

            current_time = time.time()

            display_fps = (
                1 / (current_time - self.prev_time)
                if self.prev_time != 0
                else 0
            )

            self.prev_time = current_time
                        # -----------------------------
            # Run rPPG every 5 seconds
            # -----------------------------
            if (
                self.frame_buffer.ready()
                and current_time - self.last_measurement >= 5
            ):

                frames = self.frame_buffer.get_frames()

                result = self.wrapper.process(
                    frames,
                    self.fps,
                )

                if result is not None:

                    # -----------------------------
                    # Update Heart Rate
                    # -----------------------------
                    hr = result.get("heart_rate")

                    if hr is not None:
                        self.heart_rate = f"{hr:.1f}"

                    # -----------------------------
                    # Create HealthData
                    # -----------------------------
                    health_data = HealthData(
                        heart_rate=result.get("heart_rate"),
                        hrv=result.get("hrv"),
                        respiration_rate=result.get("respiration_rate"),
                        spo2=result.get("spo2"),
                        systolic_bp=result.get("systolic_bp"),
                        diastolic_bp=result.get("diastolic_bp"),
                        body_temperature=result.get("body_temperature"),
                    )

                    # -----------------------------
                    # Estimate Blood Glucose
                    # -----------------------------
                    health_data.blood_glucose = (
                        GlucoseEstimator.estimate(
                            self.patient,
                            health_data,
                        )
                    )

                    self.latest_glucose = (
                        health_data.blood_glucose
                    )

                    # -----------------------------
                    # Evaluate Diabetes Risk
                    # -----------------------------
                    self.latest_report = (
                        self.diabetes_engine.evaluate(
                            health_data
                        )
                    )

                    report = self.latest_report

                    # -----------------------------
                    # Console Output
                    # -----------------------------
                    print("\n" + "=" * 50)
                    print("InsuGenie Diabetes Report")
                    print("=" * 50)

                    print(
                        f"Heart Rate : "
                        f"{health_data.heart_rate}"
                    )

                    print(
                        f"Estimated Glucose : "
                        f"{health_data.blood_glucose:.1f} mg/dL"
                    )

                    print(
                        f"Risk Level : "
                        f"{report.risk_level}"
                    )

                    print(
                        f"Risk Score : "
                        f"{report.score}"
                    )

                    print(
                        f"Status : "
                        f"{report.status}"
                    )

                    print("\nAlerts:")

                    if report.alerts:
                        for alert in report.alerts:
                            print(f" • {alert}")
                    else:
                        print(" • None")

                    print("\nRecommendations:")

                    for recommendation in report.recommendations:
                        print(f" • {recommendation}")

                    print("=" * 50)

                self.last_measurement = current_time
                            # -----------------------------
            # Display FPS
            # -----------------------------
            cv2.putText(
                frame,
                f"FPS: {display_fps:.1f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

            # -----------------------------
            # Display Buffer
            # -----------------------------
            cv2.putText(
                frame,
                f"Buffer: {self.frame_buffer.size()}/300",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2,
            )

            # -----------------------------
            # Display Heart Rate
            # -----------------------------
            if self.frame_buffer.ready():
                hr_text = f"{self.heart_rate} BPM"
            else:
                hr_text = "Collecting..."

            cv2.putText(
                frame,
                f"HR: {hr_text}",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
            )

            # -----------------------------
            # Display Estimated Glucose
            # -----------------------------
            if self.latest_glucose is not None:

                cv2.putText(
                    frame,
                    f"Glucose*: {self.latest_glucose:.1f} mg/dL",
                    (20, 160),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2,
                )

            # -----------------------------
            # Display Risk Level
            # -----------------------------
            if self.latest_report is not None:

                color = (0, 255, 0)

                if self.latest_report.risk_level == "Moderate":
                    color = (0, 255, 255)

                elif self.latest_report.risk_level == "High":
                    color = (0, 165, 255)

                elif self.latest_report.risk_level == "Critical":
                    color = (0, 0, 255)

                cv2.putText(
                    frame,
                    f"Risk: {self.latest_report.risk_level}",
                    (20, 200),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    color,
                    2,
                )

            # -----------------------------
            # Show Window
            # -----------------------------
            cv2.imshow("InsuGenie Camera", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()