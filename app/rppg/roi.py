import cv2


class ROIExtractor:

    @staticmethod
    def extract_forehead(frame, bbox):

        if bbox is None:
            return None

        x, y, w, h = bbox

        # Forehead coordinates
        fx = x + int(w * 0.25)
        fy = y + int(h * 0.10)

        fw = int(w * 0.50)
        fh = int(h * 0.20)

        # Crop forehead
        forehead = frame[fy:fy + fh, fx:fx + fw]

        # Safety check
        if forehead.size == 0:
            return None

        # Resize every ROI to the same dimensions
        forehead = cv2.resize(
            forehead,
            (80, 60),           # width, height
            interpolation=cv2.INTER_AREA
        )

        print("ROI after resize:", forehead.shape)

        return forehead