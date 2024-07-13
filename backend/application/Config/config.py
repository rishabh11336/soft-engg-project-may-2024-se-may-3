import os
from datetime import timedelta

class Config:
  

    Upload_Folder = os.path.join(os.getcwd(), '..', 'static')
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False