from fastapi import APIRouter

from api.general.index import router as index_router
from api.general.auth import router as auth_router
from api.general.practice import router as pr_router

routers = APIRouter()
router_list = [
    index_router,
    auth_router,
    pr_router
]

for router in router_list:
    routers.include_router(router)
