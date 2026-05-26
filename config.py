import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Application settings
    APP_NAME = os.getenv("APP_NAME")
    PORT = os.getenv("PORT")

    # VAD-specific settings
    SAMPLE_RATE = os.getenv("SAMPLE_RATE")
    FRAME_SIZE = os.getenv("FRAME_SIZE")
    ENERGY_THRESHOLD = os.getenv("ENERGY_THRESHOLD")
    MODEL_PATH = os.getenv("MODEL_PATH")

    @classmethod
    def validate(cls):
        """Validate that all required configuration keys are present."""
        missing_keys = []
        required_keys = [
            "APP_NAME",
            "PORT",
            "SAMPLE_RATE",
            "FRAME_SIZE",
            "ENERGY_THRESHOLD",
            "MODEL_PATH"
        ]

        for key in required_keys:
            if getattr(cls, key) is None:
                missing_keys.append(key)

        if missing_keys:
            raise Exception(f"Missing configuration keys: {', '.join(missing_keys)}")
