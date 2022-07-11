from fastapi import APIRouter, status

router = APIRouter(
    prefix="",
    tags=['Web Tutorial']
)

@router.get("/", status_code=status.HTTP_200_OK)
def main():
    return {"test": "test"}