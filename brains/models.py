from tortoise import Model, fields
from enums import Motion, motions, sounds


class MotionModel(Model):
    motion = fields.CharField(max_length=20,
                              null=False,
                              description=f"Motions: {list(motions)}")

    ts = fields.IntField(null=False,
                         description=f"Epoch time")

    def __str__(self):
        return f"Motion: {self.motion} Time: {self.ts}"


class SoundModel(Model):
    sound = fields.CharField(max_length=20,
                             null=False,
                             description=f"Sounds: {list(sounds)}")

    ts = fields.IntField(null=False,
                         description=f"Epoch time")

    def __str__(self):
        return f"Sounds: {self.sound} Time: {self.ts}"
