from collections import deque


class FrameBuffer:
    """
    Stores a rolling buffer of forehead ROI frames.
    """

    def __init__(self, max_frames=300):
        self.frames = deque(maxlen=max_frames)

    def add(self, frame):
        if frame is not None:
            self.frames.append(frame)

    def ready(self):
        return len(self.frames) == self.frames.maxlen

    def get_frames(self):
        return list(self.frames)

    def clear(self):
        self.frames.clear()

    def size(self):
        return len(self.frames)