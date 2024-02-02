from decouple import config

class Config:
    SECRET_KEY = config("SECRET_KEY")
    DEBUG = True
    HOST = "0.0.0.0"

config = {
    'config':Config
}

