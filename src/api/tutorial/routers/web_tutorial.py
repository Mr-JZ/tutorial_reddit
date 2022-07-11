from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(
    prefix="",
    tags=['Web Tutorial']
)

@router.get("/", status_code=status.HTTP_200_OK)
def main():
    return {"test": "test"}