from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get('/')
async def status():
    return {"status":"alive"}
