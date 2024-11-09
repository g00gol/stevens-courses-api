from fastapi import APIRouter
from courses.service import get_courses


router = APIRouter()


@router.get("/courses")
async def get():
    return await get_courses()
