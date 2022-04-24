import os

from dotenv import load_dotenv

from market import app

load_dotenv()
# Run this command to run the application in DEBUG mode.
# docker run -p 5000:5000 -e FLASK_DEBUG=1 <image-name>

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG'))
