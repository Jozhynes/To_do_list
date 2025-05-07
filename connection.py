from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

data=create_engine(path)
Session=sessionmaker(bind=data)
session=Session()