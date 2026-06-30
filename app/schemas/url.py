from datetime import datetime

from pydantic import BaseModel
from pydantic import HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl
    custom_alias: str | None = None
    expires_at: datetime | None = None


class URLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    clicks: int
    expires_at: datetime | None

    class Config:
        from_attributes = True