import json
import re
from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Optional
import yaml
from decimal import Decimal
from fastapi import File, HTTPException, UploadFile
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    StrictInt,
    StrictStr,
    confloat,
    conint,
    validator,
)
from typing import Literal
from starlette import status

class ChatReq(BaseModel):
    text_inp: str
    

class ChatRes(BaseModel):
    pl_link: str