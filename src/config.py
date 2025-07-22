from huggingface_hub import login
import os
import sys
from src.exception import CustomException
from dotenv import load_dotenv

# Load env vars
load_dotenv()  # Only needed if using a .env file locally

# Get token from env
hf_token = os.getenv("HUGGINGFACE_TOKEN")

# Login to Hugging Face
try:
    if hf_token:
        login(token=hf_token)
    else:
        raise ValueError("Missing HUGGINGFACE_TOKEN environment variable")
except Exception as e:
    raise CustomException(e,sys)

