from fastapi import APIRouter

router = APIRouter()

@router.get("/search")
async def search_books(query: str):
    return {"message": f"Searching for books with query: {query}"}
