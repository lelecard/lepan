from database import engine
from database import Base

from models import User



print("Creating database tables...")


Base.metadata.create_all(
    bind=engine
)


print("Database initialized")
