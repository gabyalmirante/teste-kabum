from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    URL = os.environ['URL']
    CEP = os.environ['CEP']