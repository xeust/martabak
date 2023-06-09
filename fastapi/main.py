import os
import time
import hashlib
from deta import Deta
from fastapi import FastAPI
from pydantic import BaseModel


def unique_string():
    seconds_of_day = int(time.time()) % 86400
    unique_hash = hashlib.sha256(str(seconds_of_day).encode('utf-8')).hexdigest()
    return unique_hash[:8]


deta = Deta()

public_pics = deta.Base(
    "blackhole_pics"
)

app = FastAPI()

class BlackholePic(BaseModel):
    type: str
    url: str

@app.post("/publish")
async def publish_blackhole_pic(blackhole_pic: BlackholePic):
    # Add the publish date and key fields
    current_time = int(time.time())
    blackhole_pic_data = blackhole_pic.dict()
    blackhole_pic_data["publish_date"] = str(current_time)
    blackhole_pic_data["key"] = str(8.64e15 - current_time) + f"-{unique_string()}"  # Very large number minus the current timestamp
    print(blackhole_pic_data)
    # Save the data to the Deta Base
    saved_blackhole_pic = public_pics.put(blackhole_pic_data)

    return {"message": "Blackhole picture published successfully", "data": saved_blackhole_pic}