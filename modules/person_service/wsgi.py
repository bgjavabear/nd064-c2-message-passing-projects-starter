import os
import logging
from app import create_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("person_service")

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    app.run(debug=True)
