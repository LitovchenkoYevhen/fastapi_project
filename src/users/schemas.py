from uuid import UUID

from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
	username: str


class UserCreate(UserBase):
	pass


class UserUpdate(BaseModel):
	pass


class UserRead(UserBase):
	id: UUID

	model_config = ConfigDict(from_attributes=True)

