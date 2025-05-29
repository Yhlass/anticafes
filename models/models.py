from sqlalchemy import *  
from sqlalchemy.orm import *
from db import Base
from datetime import datetime

class Banner(Base):
    __tablename__ = "banners"
    id = Column(Integer, primary_key=True, index=False)
    img = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, index=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    text = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    answer = relationship('Answer', back_populates='question')

class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, primary_key=True, index=False)
    text = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    question = relationship('Question', back_populates='answer')


    