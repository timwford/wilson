import asyncio

import uvicorn
from fastapi import FastAPI, HTTPException

from brains.speak import chirp, manual_noise_for_, low_beep, peep, purr
from schemas import MotionSchema, SoundSchema
from motion import move_with_, wiggle, nudge, rock
from flaxx.enum_validator import validate

app = FastAPI()

@app.get("/")
async def root():
    return {"welcome": "http://127.0.0.1:5000/docs"}

@app.post("/move")
async def move(motion: MotionSchema):
    valid, msg = validate(motion)

    if not valid:
        return HTTPException(status_code=422, detail=msg)

    await move_with_(motion.motion)

@app.post("/wiggle/fast")
async def wiggle_fast():
    await wiggle(fast=True)

@app.post("/wiggle/slow")
async def wiggle_slow():
    await wiggle(fast=False)

@app.post("/nudge")
async def nudge_forward():
    await nudge()

@app.post("/rock")
async def rock_back_and_forth():
    await rock()

@app.post("/sound")
async def make_a_sound(sound: SoundSchema):
    valid, msg = validate(sound)

    if not valid:
        return HTTPException(status_code=422, detail=msg)

    await manual_noise_for_(sound.sound)

@app.post("/chirp")
async def make_a_chirping_noise():
    await chirp()

@app.post("/low_beep")
async def make_two_low_beeps():
    await low_beep()

@app.post("/peep")
async def make_a_peeping_noise():
    await peep()

@app.post("/purr")
async def make_a_purring_noise():
    await purr()

@app.post("/attenion")
async def ask_for_attention():
    await peep(repeat=1)
    await asyncio.sleep(0.2)
    await nudge()
    await asyncio.sleep(0.2)
    await peep(repeat=2)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
