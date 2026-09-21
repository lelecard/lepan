from fastapi import APIRouter

from schemas.user import UserCreate

from services.user_service import create_user


router = APIRouter(

    prefix="/users",

    tags=["Users"]

)



@router.post("/register")
def register(
    user: UserCreate
):


    return {

        "email": user.email,

        "message":
        "User created"

    }
