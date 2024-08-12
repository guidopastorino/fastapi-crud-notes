from fastapi import APIRouter, HTTPException, status
from app.controllers.note_controller import (
    get_all_notes,
    create_note,
    update_note,
    remove_note,
)
from app.models.note_model import NoteModel
from typing import List

router = APIRouter()


@router.get("/notes", response_model=List[NoteModel])
async def read_notes():
    return await get_all_notes()


@router.post("/notes", response_model=NoteModel)
async def add_note(note: NoteModel):
    note_id = await create_note(note)
    return {**note.model_dump(), "id": note_id}


@router.put("/notes/{note_id}", response_model=int)
async def put_note(note_id: str, updated_data: dict):
    return await update_note(note_id, updated_data)


@router.delete("/notes/{note_id}", response_model=int)
async def delete_note(note_id: str):
    deleted_count = await remove_note(note_id)
    if deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return deleted_count
