from pydantic import BaseModel
from typing import Optional
from datetime import date

class CurrencyPredictionRequest(BaseModel):
    request_id: Optional[str]
    Date: Optional[date]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "request_id": "1234-04x4-894",
                "Date": "2023-04-26"
            }
        }

class CurrencyPredictionResponse(BaseModel):
    status_code: Optional[int]
    message: Optional[str]
    Date: Optional[date]
    currency: Optional[int]
    details: Optional[int]

