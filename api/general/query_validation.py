from typing import Annotated
from fastapi import Path, Query, APIRouter, Body
from pydantic import BaseModel, Field, HttpUrl
from enum import Enum


router = APIRouter(
    tags=["query_validaiton_for_reading"]
)

#query_validaiton

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@router.get("/items/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items