import os
import sys
import numpy as np

# Add rPPG-Toolbox to Python path
ROOT = os.path.dirname(__file__)
TOOLBOX = os.path.join(ROOT, "rPPG-Toolbox")

sys.path.append(TOOLBOX)

from unsupervised_methods.methods.POS_WANG import POS_WANG

# Generate fake frames
frames = np.random.randint(
    0,
    255,
    (150, 72, 72, 3),
    dtype=np.uint8
)

fps = 30

bvp = POS_WANG(frames, fps)

print("BVP length:", len(bvp))
print("First 10 values:")
print(bvp[:10])