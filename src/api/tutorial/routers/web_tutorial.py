from fastapi import APIRouter, status

router = APIRouter(
    prefix="",
    tags=['Web Tutorial']
)

@router.get("/", status_code=status.HTTP_200_OK)
def main():
    return {"root": "this is the root page, if you want to know more go to /docs"}