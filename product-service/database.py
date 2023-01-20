import sqlalchemy as database 
from sqlalchemy.orm import Session
import os
from config.constant import MODE


engine = database.create_engine(os.environ["DATABASE_URI"], echo=MODE)
session = Session()