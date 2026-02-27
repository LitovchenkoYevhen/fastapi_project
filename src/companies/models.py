import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID, uuid4

from src.models.base import Base


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
	user_id: Mapped[UUID] = mapped_column(sa.ForeignKey('user.id', ondelete="CASCADE"))
	company_id: Mapped[UUID] = mapped_column(sa.ForeignKey('company.id', ondelete="CASCADE"))
	company: Mapped['CompanyModel'] = relationship(back_populates='employees')