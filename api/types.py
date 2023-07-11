from typing import Optional
from pydantic import BaseModel

__all__ = ["RegisterReq", "UnRegisterReq", "QueryReq", "QueryReply", "StatusReply"]


class RegisterReq(BaseModel):
    flow_uuid: str
    model: list
    backend: list
    zoo: str


class UnRegisterReq(BaseModel):
    flow_uuid: str


class QueryReq(BaseModel):
    flow_uuid: str
    image_base64: str


class QueryReply(BaseModel):
    error_code: int
    msg: str
    face: Optional[list] = None
    object: Optional[list] = None
    ocr: Optional[list] = None
    cls: Optional[list] = None
    anime: Optional[str] = None
    tddfa: Optional[str] = None
    key_points: Optional[list] = None


class StatusReply(BaseModel):
    error_code: int
    msg: str
