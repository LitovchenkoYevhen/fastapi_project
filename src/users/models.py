from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID, uuid4

from src.models.base import Base


if TYPE_CHECKING:
	from src.companies.models import EmployeeModel


class UserModel(Base):
	__tablename__ = 'user'
	id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
	username: Mapped[str] = mapped_column(sa.String(), unique=True)
	profile: Mapped['ProfileModel'] = relationship(
		back_populates='user',
		cascade="all, delete-orphan",
		uselist=False
	)
	employee: Mapped['EmployeeModel'] = relationship(
		back_populates='user',
		uselist=False
	)


class ProfileModel(Base):
	__tablename__ = 'profile'
	id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
	name: Mapped[str] = mapped_column(sa.String())
	email: Mapped[str] = mapped_column(sa.String())
	user_id: Mapped[UUID] = mapped_column(sa.ForeignKey('user.id', ondelete='CASCADE'),
										  unique=True)  #  unique=True дает One 2 One
	user: Mapped['UserModel'] = relationship(
		back_populates='profile'
	)
