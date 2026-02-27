import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeMeta, declarative_base

# Рекомендованная конвенция именования для индексов и ограничений
POSTGRES_INDEXES_NAMING_CONVENTION = {
	"ix": "%(column_0_label)s_idx",
	"uq": "%(table_name)s_%(column_0_name)s_key",
	"ck": "%(table_name)s_%(constraint_name)s_check",
	"fk": "%(table_name)s_%(column_0_name)s_fkey",
	"pk": "%(table_name)s_pkey",
}

metadata = sa.MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)


class BaseServiceModel:
	"""Базовый класс для таблиц сервиса."""

	@classmethod
	def on_conflict_constraint(cls) -> tuple | None:
		return None


Base: DeclarativeMeta = declarative_base(metadata=metadata, cls=BaseServiceModel)
