import time
from math import floor

class SMPTETimecode:
    def __init__(self, framerate=25):
        self.set_framerate(framerate)
        self.start_time = time.time()

    def set_framerate(self, framerate):
        allowed_framerates = [23.976, 24, 25, 29.97, 30, 50, 59.94, 60]
        if framerate not in allowed_framerates:
            raise ValueError(f"Unsupported frame rate. Choose from {allowed_framerates}")
        self.framerate = framerate

    def current_timecode(self):
        elapsed = time.time() - self.start_time
        total_frames = floor(elapsed * self.framerate)
        hours = total_frames // (3600 * int(self.framerate))
        minutes = (total_frames // (60 * int(self.framerate))) % 60
        seconds = (total_frames // int(self.framerate)) % 60
        frames = total_frames % int(self.framerate)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{frames:02d}"
