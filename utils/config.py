import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # --- URLs ---
    UI_BASE_URL: str = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
    API_BASE_URL: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

    # --- Credentials ---
    STANDARD_USER: str = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_USER: str = os.getenv("LOCKED_USER", "locked_out_user")
    PROBLEM_USER: str = os.getenv("PROBLEM_USER", "problem_user")
    PASSWORD: str = os.getenv("PASSWORD", "secret_sauce")

    # --- Browser settings ---
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO: int = int(os.getenv("SLOW_MO", "0"))
    TIMEOUT: int = int(os.getenv("TIMEOUT", "10000"))  # ms
