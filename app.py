from contextlib import asynccontextmanager

from starlette.routing import Match

from src.config.logger_conf import logger
from src.config.api_conf import api_settings
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from src.router.include_routers import init_routers
scheduler = AsyncIOScheduler()


@asynccontextmanager
async def lifespan(_: FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(
    title='Backend for Internet Shop',
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=api_settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*'],
)
@app.middleware('http')
async def log_middle(request: Request, call_next):
    logger.debug(f'{request.method} {request.url}')
    routes = request.app.router.routes
    logger.debug('Params:')
    for route in routes:
        match, scope = route.matches(request)
        if match == Match.FULL:
            for name_params, value_params in scope['path_params'].items():
                logger.debug(f'\t{name_params}: {value_params}')
    logger.debug('Headers:')
    for name_header, value_header in request.headers.items():
        logger.debug(f'\t{name_header}: {value_header}')

    return await call_next(request)

init_routers(app)