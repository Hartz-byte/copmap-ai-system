from pydantic import BaseModel

class ImageRequest(BaseModel):
    image_path: str
    location: str
    timestamp: str

class SummaryRequest(BaseModel):
    query: str
