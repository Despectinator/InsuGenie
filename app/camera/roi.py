import cv2


class ROIExtractor:
    """
    Extracts the forehead region from a detected face.
    """

    ROI_WIDTH = 80
    ROI_HEIGHT = 60

    @staticmethod
    def extract_forehead(frame, bbox):

        if bbox is None:
            return None

        x, y, w, h = bbox

        # Forehead region
        fx = x + int(w * 0.25)
        fy = y + int(h * 0.10)

        fw = int(w * 0.50)
        fh = int(h * 0.20)

        # -----------------------------
        # Keep ROI inside image
        # -----------------------------
        img_h, img_w = frame.shape[:2]

        fx = max(0, fx)
        fy = max(0, fy)

        fw = min(fw, img_w - fx)
        fh = min(fh, img_h - fy)

        if fw <= 0 or fh <= 0:
            return None

        # Extract ROI
        forehead = frame[fy:fy + fh, fx:fx + fw]

        # Empty ROI check
        if forehead.size == 0:
            return None

        # -----------------------------
        # Resize every ROI
        # -----------------------------
        forehead = cv2.resize(
            forehead,
            (ROIExtractor.ROI_WIDTH, ROIExtractor.ROI_HEIGHT),
            interpolation=cv2.INTER_AREA
        )

        return forehead