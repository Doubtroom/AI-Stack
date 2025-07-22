from huggingface_hub import login
import os
import sys
from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv

try:
    load_dotenv()  # Loads variables from a local .env file (only in dev environments)
    
    hf_token = os.getenv("HUGGINGFACE_TOKEN", "").strip()  # Clean any accidental spaces

    if not hf_token:
        raise ValueError("Missing HUGGINGFACE_TOKEN environment variable")

    login(token=hf_token)
    logging.info("[INFO] Successfully logged into Hugging Face Hub.")

except Exception as e:
    raise CustomException(e, sys)
