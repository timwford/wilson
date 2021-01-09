from models import MotionModel, SoundModel
from flaxx.pydantic_schema_generator import pydantic_model_creator

MotionSchema = pydantic_model_creator(MotionModel, exclude_pk=True, exclude=('ts',))
SoundSchema = pydantic_model_creator(SoundModel, exclude_pk=True, exclude=('ts',))
