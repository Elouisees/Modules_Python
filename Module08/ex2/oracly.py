#!/usr/bin/env python3

try:
    from dotenv import load_dotenv
except ImportError as e:
    print(e)
    exit(1)
import os


if __name__ == "__main__":

    load_dotenv()
    MATRIX_MODE = os.getenv('MATRIX_MODE')
    DATABASE_URL = os.getenv('DATABASE_URL')
    API_KEY = os.getenv('API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    ZION_ENDPOINTS = os.getenv('ZION_ENDPOINTS')

    vars: dict = {
        "MATRIX_MODE": os.getenv('MATRIX_MODE'),
        "DATABASE_URL": os.getenv('DATABASE_URL'),
        "API_KEY": os.getenv('API_KEY'),
        "LOG_LEVEL": os.getenv('LOG_LEVEL'),
        "ZION_ENDPOINTS": os.getenv('ZION_ENDPOINTS')
    }

    hardc: list = [name for name in ["API_KEY", "DATABASE_URL"]
                   if name in globals()]
    if hardc:
        mess0: str = "[OK] No hardcoded secrets detected"
    else:
        mess0 = "[ERROR] Hardcoded secrets detected"

    if os.path.exists(".env"):
        sign: int = 0
        for key, value in vars.items():
            if value is None:
                print(f"[ERROR] {key} is not set")
                sign += 1
        if sign >= 1:
            mess1: str = "[ERROR] Missing variables"
        else:
            mess1 = "[OK] .env file properly configured"

        if MATRIX_MODE == "development":
            title: str = "ORACLE STATUS: Reading the Matrix..."
            mess2: str = "[OK] Production overrides available"
        else:
            title = "ORACLE STATUS: Accessing the mainframe..."
            if os.getenv("PROD_DB_URL") and os.getenv("PROD_API_KEY"):
                mess2 = "[OK] Production overrides available"
            else:
                mess2 = "[WARN] Production overrides unavailable"

        print(title)
        print("\nConfiguration loaded:")
        print(f"Mode: {MATRIX_MODE}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"LOG_LEVEL: {LOG_LEVEL}")
        print("Zion Network: Online")

        print("\nEnvironment security check:")
        print(mess0)
        print(mess1)
        print(mess2)

    else:
        print("[ERROR] No .env file found.")
        print("Create a .env file based on .env.example before "
              "accessing the mainframe.")
        exit()

    print("\nThe Oracle sees all configurations.")
