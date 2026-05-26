from config import Config
Config.validate()

print("Application Started")
print("Project Name:", Config.APP_NAME)
print("Port:", Config.PORT)
print("Sample Rate:", Config.SAMPLE_RATE)
print("Frame Size:", Config.FRAME_SIZE)
print("Energy Threshold:", Config.ENERGY_THRESHOLD)
