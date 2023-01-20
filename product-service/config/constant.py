import os 
from dotenv import load_dotenv

load_dotenv()
DATABASE_URI = os.environ["DATABASE_URI"]
MODE= True if os.environ["MODE"] == "development" else False 