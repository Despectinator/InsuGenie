import numpy as np

from app.rppg.wrapper import RPPGWrapper

frames = np.random.randint(
    0,
    255,
    (300, 60, 80, 3),
    dtype=np.uint8
)

wrapper = RPPGWrapper()

wrapper.process(frames, 30)