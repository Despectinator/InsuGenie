import cv2


class FaceDetector:

    def __init__(self):

        print("Using detector: OpenCV Haar Cascade")

        cascade_path = (
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

        self.detector = cv2.CascadeClassifier(cascade_path)

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.detector.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=4,
            minSize=(100, 100)
        )

        if len(faces) == 0:
            return frame, None

        # Use the largest detected face
        x, y, w, h = max(
            faces,
            key=lambda f: f[2] * f[3]
        )

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        return frame, (x, y, w, h)