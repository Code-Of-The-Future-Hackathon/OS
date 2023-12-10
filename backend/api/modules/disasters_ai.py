from fastapi import APIRouter
import drought as drought
import flood as flood
import landslide as landslide
import wildfire as wildfire

router = APIRouter()

# @router.post("/ai/disasters/landslides", tags=["Disasters AI"])
# async def predict_landslides(latitude: float, longtitude: float):
#     request = ""
#     prediction = landslide.predict(data)

    