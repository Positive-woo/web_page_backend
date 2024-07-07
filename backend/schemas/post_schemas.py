from pydantic import BaseModel
from datetime import datetime, date, time
from typing import Optional
import json


class Post_base(BaseModel):
    post_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PostInfo_read(Post_base):
    title: str
    section: str
    continuous_recruit: bool
    start_date: Optional[date]
    end_date: date
    full_time: bool
    specific: bool
    task: Optional[str]
    weekdays: bool
    work_start: time
    work_end: time
    work_spot: Optional[str]
    apply_online_url: Optional[str]
    deleted: bool
    qualification: Optional[str]
    preferred: Optional[str]


class PostInfo_create(BaseModel):
    title: str
    section: str
    continuous_recruit: bool
    start_date: Optional[date]
    end_date: date
    full_time: bool
    specific: bool
    task: Optional[str]
    weekdays: bool
    work_start: time
    work_end: time
    work_spot: Optional[str]
    apply_online_url: Optional[list[str]] = []
    deleted: bool = False
    qualification: Optional[list[str]] = []
    preferred: Optional[list[str]] = []
