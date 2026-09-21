from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func
from sqlalchemy import DateTime


from database import Base



class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    email = Column(
        String,
        unique=True,
        index=True
    )


    password_hash = Column(
        String
    )


    plan = Column(
        String,
        default="free"
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )
