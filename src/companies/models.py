from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID, uuid4
from src.models.base import Base

if TYPE_CHECKING:
	from src.users.models import UserModel

class CompanyModel(Base):
	__tablename__ = 'company'
	id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
	name: Mapped[str] = mapped_column(sa.String())

	employees: Mapped[list['EmployeeModel']] = relationship(
		back_populates='company',
		cascade='all, delete-orphan',
	)


class EmployeeModel(Base):
	__tablename__ = 'employee'
	id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
	user_id: Mapped[UUID] = mapped_column(sa.ForeignKey('user.id', ondelete="CASCADE"), unique=True)
	company_id: Mapped[UUID] = mapped_column(sa.ForeignKey('company.id', ondelete="CASCADE"))  # объявляем FK
	company: Mapped['CompanyModel'] = relationship(back_populates='employees')  # ОТДЕЛЬНО еще объявляем связь
	user: Mapped['UserModel'] = relationship(
		back_populates='employee',
	)
