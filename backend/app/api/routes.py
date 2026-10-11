from fastapi import APIRouter, HTTPException
from typing import List
from ..models.model import HeatwaveData
from ..services.service import get_heatwave_data

router = APIRouter()

@router.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "healthy"}

@router.get("/heatwaves", response_model=List[HeatwaveData], tags=["Heatwave Data"])
async def read_heatwave_data(region: str):
    try:
        data = await get_heatwave_data(region)
        if not data:
            raise HTTPException(status_code=404, detail="No heatwave data found for the specified region.")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))