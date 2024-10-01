from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# This will store the locations in memory (you can replace it with a database)
locations_db = []

# Define the model for location data
class Location(BaseModel):
    latitude: float
    longitude: float
    message: str

# API endpoint to post a location
@app.post("/post-location")
async def post_location(location: Location):
    # Append the location to the in-memory "database"
    locations_db.append(location)
    
    # For now, print it to the console (you can later store it in a database)
    print(f"Received location: {location.latitude}, {location.longitude}, {location.message}")
    
    # Return a response
    return {"status": "Location saved", "location": location}

# API endpoint to get all locations
@app.get("/locations", response_model=List[Location])
async def get_locations():
    # Return the list of saved locations
    return locations_db
