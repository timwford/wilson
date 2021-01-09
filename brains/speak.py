import asyncio

from brains.enums import Sound
from motion import ser


async def manual_noise_for_(sound: str):
    ser.write(str.encode(sound))


async def chirp():
    ser.write(str.encode(Sound.HIGH_FAST.value))
    ser.write(str.encode(Sound.LOW_FAST.value))
    ser.write(str.encode(Sound.HIGH_SLOW.value))


async def low_beep():
    ser.write(str.encode(Sound.LOW_SLOW.value))
    ser.write(str.encode(Sound.LOW_SLOW.value))


async def peep(repeat: int = 3):
    for i in range(repeat):
        ser.write(str.encode(Sound.HIGH_FAST.value))
        ser.write(str.encode(Sound.HIGH_FAST.value))
        ser.write(str.encode(Sound.HIGH_FAST.value))


async def purr(repeat: int = 2):
    for i in range(repeat):
        ser.write(str.encode(Sound.LOW_SLOW.value))
        await asyncio.sleep(0.2)
        ser.write(str.encode(Sound.HIGH_SLOW.value))
        await asyncio.sleep(0.2)
        ser.write(str.encode(Sound.LOW_SLOW.value))
        await asyncio.sleep(0.5)
