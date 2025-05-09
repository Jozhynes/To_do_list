from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
path='patrick'@'lacalhost'
data=create_engine(path)
Session=sessionmaker(bind=data)
session=Session()