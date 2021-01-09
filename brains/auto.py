import asyncio
import uvloop

from brains.speak import chirp


class BaseState:
    def __init__(self):
        self.satisfied = False
        self.zenny = False
        self.worthy = False


class Brain:
    def __init__(self):
        print("Brain created")
        self.satisfied = 100  # battery, timers for light calibration/etc
        self.zen = 50  # quiet, sleep, zen, meditation, darkness
        self.worth = 50  # attention

        self.baseState = BaseState()

    def __str__(self):
        return f"Hunger: {self.satisfied} Zen: {self.zen} Worth: {self.worth}"

    def update_base_state(self):
        # check physical needs, assume percentage of 100
        if self.satisfied > 20:
            self.baseState.satisfied = True
        else:
            self.baseState.satisfied = False

        if self.zen > 65:
            self.baseState.zenny = True
        else:
            self.baseState.zenny = False

        if self.worth > 50:
            self.baseState.worthy = True
        else:
            self.baseState.worthy = False

    async def step(self):
        self.update_base_state()

        if self.baseState.satisfied:
            if self.baseState.zenny:
                if self.baseState.worthy:
                    print("Perfect")
                else:
                    print("Worth")
            else:
                print("Zen")
        else:
            print("Hungry")


async def main():
    brain = Brain()

    while True:
        await brain.step()
        await asyncio.sleep(1)


uvloop.install()
asyncio.run(main())
