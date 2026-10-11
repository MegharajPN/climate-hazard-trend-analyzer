from pydantic import BaseModel
from typing import List, Optional

class HeatwaveData(BaseModel):
    region: str
    start_date: str
    end_date: str
    duration: int
    intensity: float

class HeatwaveResponse(BaseModel):
    heatwaves: List[HeatwaveData]
    total_heatwaves: int

class TrendAnalysisRequest(BaseModel):
    region: str
    start_year: int
    end_year: int

class TrendAnalysisResponse(BaseModel):
    region: str
    trend: str
    data: List[HeatwaveData]