from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func

Base = declarative_base()



#--------------------------------------------------



class User (Base):
    __tablename__ = 'user' 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password_hash = Column(String)
    apps = relationship("App", back_populates="user")
    comments = relationship("commentory", back_populates="user"
#
 #   def hash_password(self, password):
  #      self.password_hash = pwd_context.encrypt(password)

   # def verify_password(self, password):
    #    return pwd_context.verify(password, self.password_hash)

class Commentory (Base):
    __tablename__ = 'commentory'
    id = Column(Integer, primary_key=True)
    date = Column(Integer, Integer, Integer)
    content = Column(String)
    user = relationship("user", back_populates="commentory"

class App (Base):
    __tablename__ = 'app'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    user = relationship("User", back_populates="apps")
    date = Column(Integer)

































#------------------------------------------------------------------




engine = create_engine('sqlite:///FirstDB.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()