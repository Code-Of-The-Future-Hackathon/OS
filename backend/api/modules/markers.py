from fastapi import APIRouter

router = APIRouter()

@router.get("/markers", tags=["Markers"])
def get_markers():
    # marker coordinates: [latitude, longitude]
    return {
        "markers": [
            {
                "coordinates": [40.270345, -7.702399],
                "type": "Flood"
            },
            {
                "coordinates": [38.228201, -3.575201],
                "type": "Flood"
            },
            {
                "coordinates": [44.362028, 1.453241],
                "type": "Drought"
            },
            {
                "coordinates": [48.269465, 6.995383],
                "type": "Flood"
            },
            {
                "coordinates": [50.081630, 2.401828],
                "type": "Wildfire"
            },
            {
                "coordinates": [53.580812, -2.251204],
                "type": "Landslide"
            },
            {
                "coordinates": [52.589505, 1.542940],
                "type": "Flood"
            },
            {
                "coordinates": [44.569839, 9.637719],
                "type": "Wildfire"
            },
            {
                "coordinates": [41.316657, 16.291636],
                "type": "Flood"
            },
            {
                "coordinates": [41.845051, 20.989483],
                "type": "Landslide"
            },
            {
                "coordinates": [44.926542, 27.271984],
                "type": "Landslide"
            },
            {
                "coordinates": [42.971855, 26.763780],
                "type": "Drought"
            },
            {
                "coordinates": [49.303164, 21.677162],
                "type": "Flood"
            },
            {
                "coordinates": [54.194233, 20.625644],
                "type": "Landslide"
            },
            {
                "coordinates": [51.850261, -7.824125],
                "type": "Drought"
            },
            {
                "coordinates": [60.989764, 13.504405],
                "type": "Wildfire"
            },
            {
                "coordinates": [59.627495, 5.442548],
                "type": "Landslide"
            }
        ]
    }

@router.get("/markers/{type}", tags=["Markers"])
def get_markers_by_type(type: str):
    if type == "landslide":
        return {
            "markers": [
                {
                    "coordinates": [53.580812, -2.251204],
                    "type": "Landslide"
                },
                {
                    "coordinates": [41.845051, 20.989483],
                    "type": "Landslide"
                },
                {
                    "coordinates": [44.926542, 27.271984],
                    "type": "Landslide"
                },
                {
                    "coordinates": [54.194233, 20.625644],
                    "type": "Landslide"
                },
                {
                    "coordinates": [59.627495, 5.442548],
                    "type": "Landslide"
                }
            ]
        }
    elif type == "flood":
        return {
            "markers": [
                {
                    "coordinates": [40.270345, -7.702399],
                    "type": "Flood"
                },
                {
                    "coordinates": [38.228201, -3.575201],
                    "type": "Flood"
                },
                {
                    "coordinates": [48.269465, 6.995383],
                    "type": "Flood"
                },
                {
                    "coordinates": [52.589505, 1.542940],
                    "type": "Flood"
                },
                {
                    "coordinates": [41.316657, 16.291636],
                    "type": "Flood"
                },
                {
                    "coordinates": [49.303164, 21.677162],
                    "type": "Flood"
                }
            ]
        }
    elif type == "wildfire":
        return {
            "markers": [
                {
                    "coordinates": [50.081630, 2.401828],
                    "type": "Wildfire"
                },
                {
                    "coordinates": [44.569839, 9.637719],
                    "type": "Wildfire"
                },
                {
                    "coordinates": [60.989764, 13.504405],
                    "type": "Wildfire"
                }
            ]
        }
    elif type == "drought":
        return {
            "markers": [
                {
                    "coordinates": [44.362028, 1.453241],
                    "type": "Drought"
                },
                {
                    "coordinates": [42.971855, 26.763780],
                    "type": "Drought"
                },
                {
                    "coordinates": [51.850261, -7.824125],
                    "type": "Drought"
                }
            ]
        }