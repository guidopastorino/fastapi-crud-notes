from app.db.mongodb import note_collection
from app.models.note_model import NoteModel
from bson import ObjectId
from datetime import datetime, timezone


# Función para obtener todas las notas
async def get_all_notes():
    notes = []
    async for document in note_collection.find():
        # Convertir ObjectId a string
        document["_id"] = str(document["_id"])
        notes.append(NoteModel(**document))
    return notes


# Función para crear una nota
async def create_note(note: NoteModel):
    note_dict = note.model_dump(by_alias=True)
    note_dict["_id"] = ObjectId()  # Generar un nuevo ObjectId si no está presente
    note_dict["created_at"] = datetime.now(
        timezone.utc
    )  # Establecer la fecha de creación
    result = await note_collection.insert_one(note_dict)
    return str(result.inserted_id)


# Actualizar una nota
async def update_note(note_id: str, updated_data: dict) -> int:
    note = await note_collection.find_one({"_id": ObjectId(note_id)})

    if not note:
        return None

    if "version_history" not in note:
        note["version_history"] = []

    note["version_history"].append(
        {
            "updated_at": (
                note["updated_at"] if note["updated_at"] else note["created_at"]
            ),
            "title": note["title"],
            "content": note["content"],
        }
    )

    # Actualizar los campos de la nota
    note.update(updated_data)
    note["updated_at"] = datetime.now(timezone.utc)

    result = await note_collection.replace_one({"_id": ObjectId(note_id)}, note)
    return result.modified_count


# Eliminar una nota
async def remove_note(note_id: str) -> int:
    result = await note_collection.delete_one({"_id": ObjectId(note_id)})
    return result.deleted_count
