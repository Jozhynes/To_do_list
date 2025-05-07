from model import base
from connection import data
Base.metadata.create_all(bind=data)