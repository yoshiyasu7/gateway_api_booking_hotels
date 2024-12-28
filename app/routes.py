from fastapi import APIRouter, HTTPException, Response, Depends

from app.security_settings import security, config
from app.schemas import UserLoginSchema
from app.services.booking import get_bookings
from app.services.hotels import get_hotels

router = APIRouter()

@router.post("/login")
def login(credentials: UserLoginSchema, response: Response):
    if credentials.email == "admin@gmail.com" and credentials.password == "admin":
        token = security.create_access_token(uid=credentials.email)
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect email or password")

@router.get("/get_hotels", dependencies=[Depends(security.access_token_required)])
async def hotels_endpoint():
    data = await get_hotels()
    return {"data": data}


@router.get("/get_bookings", dependencies=[Depends(security.access_token_required)])
async def bookings_endpoint():
    data = await get_bookings()
    return {"data": data}
