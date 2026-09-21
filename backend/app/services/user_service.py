from sqlalchemy.orm import Session

from models import User

from security import hash_password



def create_user(
    db: Session,
    email: str,
    password: str
):


    password_hash = hash_password(
        password
    )


    user = User(

        email=email,

        password_hash=password_hash,

        plan="free"

    )


    db.add(user)

    db.commit()

    db.refresh(user)


    return user



def get_user_by_email(
    db: Session,
    email: str
):


    return db.query(User).filter(

        User.email == email

    ).first()
