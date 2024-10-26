import os
from dotenv import load_dotenv

load_dotenv()

jwt_infos = {
    "KEY": os.environ.get("JWT_SECRET_KEY"),
    "ALGORITHM": os.environ.get("ALGORITHM"),
    "JWT_HOURS": os.environ.get("JWT_HOURS")
}