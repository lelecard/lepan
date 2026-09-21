from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.post("/register")
def register():

    return {

        "message":
        "User registration API ready"

    }
