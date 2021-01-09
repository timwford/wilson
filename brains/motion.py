import serial

from brains.enums import Motion
import asyncio

ser = serial.Serial('/dev/cu.usbmodem144201')


async def move_with_(motion: str, duration: float = None):
    ser.write(str.encode(motion))

    if duration is not None:
        await asyncio.sleep(duration)
        ser.write(str.encode(Motion.HALT.value))


async def wiggle(fast: bool = False, repeat: int = 3):
    if fast:
        for i in range(repeat):
            await move_with_(Motion.LEFT.value, duration=0.2)
            await move_with_(Motion.RIGHT.value, duration=0.2)
    else:
        for i in range(repeat):
            await move_with_(Motion.LEFT.value, duration=0.7)
            await move_with_(Motion.RIGHT.value, duration=0.7)


async def nudge():
    await move_with_(Motion.FORWARD.value, duration=0.45)
    await move_with_(Motion.BACKWARD.value, duration=0.3)


async def rock(repeat: int = 3):
    for i in range(repeat):
        await move_with_(Motion.FORWARD.value, duration=0.2)
        await move_with_(Motion.BACKWARD.value, duration=0.2)
