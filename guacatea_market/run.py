
# Core libraries
import os

# Third libraries
from dotenv import load_dotenv

# owner libraries
from market import app


load_dotenv()

# Checa si el run.py ha sido ejecutado directamente y no importado
if __name__ == '__main__':
    PORT = int(os.getenv("FLASK_RUN_PORT", 5000))
    HOST = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    DEBUG = os.getenv("DEBUG", False)

    app.run(host=HOST, port=PORT, debug=DEBUG)
    
