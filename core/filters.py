"""Signal filtering and smoothing utilities."""

from collections import deque
import numpy as np


class LowPassFilter:
    """2nd-order moving weighted filter to eliminate coordinate jitter."""

    def __init__(self, cutoff_samples: int = 5):
        self.buffer = deque(maxlen=cutoff_samples)

    def update(self, val: float) -> float:
        self.buffer.append(val)
        weights = np.linspace(0.5, 1.0, len(self.buffer))
        weights /= weights.sum()
        return float(np.sum(np.array(self.buffer) * weights))

    def clear(self):
        self.buffer.clear()
