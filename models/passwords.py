from sqlalchemy import UUID, ForeignKey, Integer, String, Boolean, Column
from database import Base
from models.users import Users

class Passwords(Base):
    __tablename__ = "passwords"

    id = Column(UUID, primary_key=True, index=True,)
    user_id = Column(UUID, ForeignKey("Users.id"))
    password = Column(Integer,nullable=False)