import os
from dotenv import load_dotenv
from src.app.server.server import app

from src.configs.base import Base
from src.configs.connection import db_connection_handler

db_connection_handler.connect_to_db(Base)

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT",3000)),
        debug=os.environ.get("DEBUG", False)
    )
