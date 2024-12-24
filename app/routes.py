from fastapi import APIRouter

from app.services.booking_hotels import get_hotels

router = APIRouter()

@router.get("/get_hotels")
async def booking_hotels_endpoint():
    data = await get_hotels()
    return {"data": data}
