from fastapi import APIRouter

from api.general.index import router as index_router
from api.general.practice import router as pr_router
from api.general.path_prac import router as path_router
from api.general.query_prac import router as query_router
from api.general.body_prac import router as body_router
from api.general.query_validation import router as q_v_router

routers = APIRouter()
router_list = [
    index_router,
    pr_router,
    path_router,
    query_router,
    body_router,
    q_v_router
]

for router in router_list:
    routers.include_router(router)
