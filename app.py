from config import Config

Config.validate()

print("Application Started")
print("Project Name:", Config.APP_NAME)
print("Port:", Config.PORT)
print("Sample Rate:", Config.SAMPLE_RATE)
print("Frame Size:", Config.FRAME_SIZE)
print("Energy Threshold:", Config.ENERGY_THRESHOLD)
ENERGY_THRESHOLD = Config.ENERGY_THRESHOLD
MIN_SPEECH_FRAMES = 5
speech_frames = 0
energy = 600  
if energy > ENERGY_THRESHOLD:
    speech_frames += 1
else:
    speech_frames = 0

speech_detected = False

if speech_frames >= MIN_SPEECH_FRAMES:
    speech_detected = True

print("Speech Detected:", speech_detected)
