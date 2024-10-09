import os

jwt_infos = {
    "KEY": os.getenv("JWT_SECRET_KEY"),
    "ALGORITHM": os.getenv("ALGORITHM"),
    "JWT_HOURS": os.getenv("JWT_HOURS")
}