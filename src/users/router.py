from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from src.users.models import UserModel
from src.users.schemas import UserCreate, UserRead
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/create', response_model=UserRead)
async def create_user(
    user_create_: UserCreate,
    session: AsyncSession = Depends(get_session)
) -> UserModel:
    new_user = UserModel(**user_create_.model_dump())
    session.add(new_user)
    # commit is handled by get_session dependency in src/db.py
    await session.flush()
    await session.refresh(new_user)
    return new_user
