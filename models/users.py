from sqlalchemy import UUID, ForeignKey, String, Boolean, Column
from database import Base
from models.passwords import Passwords

class Users(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True,)
    name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    patronymic = Column(String,nullable=True)
    phone = Column(String,nullable=False)
    password_id = Column(UUID,ForeignKey("Passwords.id"),nullable=False)
    avatar = Column(String,nullable=False)
    is_verified = Column(Boolean, nullable=False)
