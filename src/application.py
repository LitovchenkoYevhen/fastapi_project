from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.healthcheck.router import router as healthcheck_router
from src.users.router import router as user_router

# Импорт моделей для инициализации связей SQLAlchemy
from src.users.models import UserModel, ProfileModel
from src.companies.models import CompanyModel, EmployeeModel
from src.projects.models import ProjectModel, TechnologyModel

def get_app() -> FastAPI:
	"""
	Get FastAPI application.

	This is the main constructor of an application.

	:return: application.
	"""
	app = FastAPI(
		docs_url='/docs',
		openapi_url='/openapi.json',
		default_response_class=UJSONResponse,
	)

	app.add_middleware(
		CORSMiddleware,
		allow_origins=['*'],
		allow_credentials=True,
		allow_methods=['*'],
		allow_headers=['*'],
	)
	app.include_router(healthcheck_router)
	app.include_router(user_router)

	return app
