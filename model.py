from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ToDoList(Base):
    __tablename__ = 'to_do_list'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(100))
    description = Column(String(100))
    completed = Column(Boolean, default=False)

    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
        