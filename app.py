from config import Config
import numpy as np

Config.validate()

ENERGY_THRESHOLD = float(Config.ENERGY_THRESHOLD)

LOW_ZCR_THRESHOLD = 0.02
NOISE_THRESHOLD = 50
MIN_SPEECH_FRAMES = 5


def calculate_energy(frame):
    return np.sum(frame ** 2)


def calculate_zcr(frame):
    return np.mean(np.abs(np.diff(np.sign(frame)))) / 2


def detect_speech(frames):

    speech_frames = 0

    for frame in frames:

        energy = calculate_energy(frame)
        zcr = calculate_zcr(frame)

        if zcr < LOW_ZCR_THRESHOLD:
            continue

        if energy < NOISE_THRESHOLD:
            continue

        if energy > ENERGY_THRESHOLD:
            speech_frames += 1
        else:
            speech_frames = 0

        if speech_frames >= MIN_SPEECH_FRAMES:
            return True

    return False


sample_frames = [
    np.random.randn(320) * 100
    for _ in range(10)
]

speech_detected = detect_speech(sample_frames)

print("Speech Detected:", speech_detected)
