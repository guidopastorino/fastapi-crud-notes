from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class NoteModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    tags: Optional[List[str]] = []
    is_favorite: bool = False
    is_archived: bool = False
    due_date: Optional[datetime] = None
    version_history: Optional[List[dict]] = []
