import os
from dotenv import load_dotenv
from src.app.server.server import app

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",3000)), debug=True)
