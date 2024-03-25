from typing import Annotated
from fastapi import Path, Query, APIRouter, Body
from pydantic import BaseModel, Field, HttpUrl

router = APIRouter(
    tags=["practice_for_reading"]
)

#簡略設計專輯小卡交換登記系統



class Image(BaseModel):   #可以放上專輯照片連結(不放也可以)
    url: HttpUrl
    name: str

class Card(BaseModel):
    group_name: str
    member_name: str | None = None
    price: int = Field(gt=0, le=500, description="The price must be less or equal than 500")
    tags: set[str] = set()
    image: list[Image] | None = None
    description: str | None = Field(default=None, title="The description of the card", max_length=55)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "group_name": "IVE",
                    "member_name": "Liz",
                    "price": 500,
                    "tags": ["eleven", "love dive"],
                    "description": "Condition is good",
                }
            ]
        }
    }


class User(BaseModel):
    username: str
    contact_id: str = Field(description="your phone/email or lind id")


@router.get("/{card_id}")
def read_card(
    card_id: Annotated[int, Path(title="The ID of the card to get", gt=0, le=45)],
    q: Annotated[str | None, Query(alias="group_name")] = None,
):
    results = {"card_id": card_id}
    if q:
        results.update({"q": q})
    return results


@router.post("/{card_id}")
def create_item(
    card_id: int, item: Annotated[Card, Body(embed=True)], user: User
):
    results = {"card_id": card_id, "item": item, "user": user}
    return results