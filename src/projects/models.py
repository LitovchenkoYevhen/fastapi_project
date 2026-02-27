import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID, uuid4

from src.models.base import Base


project_technology_association_table = sa.Table(
    'project_technology_association',
	Base.metadata,
	sa.Column('project_id', sa.Uuid, ForeignKey('project.id', ondelete="CASCADE"), primary_key=True),
	sa.Column('technology_id', sa.Uuid, ForeignKey('technology.id', ondelete="CASCADE"), primary_key=True),
)


class ProjectModel(Base):
	__tablename__ = 'project'
	id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
	name: Mapped[str] = mapped_column(sa.String())
	technologies: Mapped[list['TechnologyModel']] = relationship(
		secondary=project_technology_association_table,
		back_populates='projects',
	)


class TechnologyModel(Base):
	__tablename__ = 'technology'
	id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
	name: Mapped[str] = mapped_column(sa.String())

	projects: Mapped[list['ProjectModel']] = relationship(
		secondary=project_technology_association_table,
		back_populates='technologies',
	)