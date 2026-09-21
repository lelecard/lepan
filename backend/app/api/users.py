from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session


from database import get_db

from schemas.user import UserCreate

from services.user_service import create_user



router = APIRouter(

    prefix="/users",

    tags=["Users"]

)



@router.post("/register")
def register(

    user: UserCreate,

    db: Session = Depends(get_db)

):


    new_user = create_user(

        db,

        user.email,

        user.password

    )


    return {

        "id": new_user.id,

        "email": new_user.email,

        "plan": new_user.plan

    }
