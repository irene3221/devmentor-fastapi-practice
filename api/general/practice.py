from typing import Annotated
from fastapi import Path, Query, APIRouter, Body
from pydantic import BaseModel, Field, HttpUrl

router = APIRouter(
    tags=["practice_for_reading"]
)

#簡略設計專輯小卡交換登記系統
#盡量把那些function都用到



class Image(BaseModel):   #可以放上專輯照片連結(不放也可以)
    url: HttpUrl
    name: str

class Card(BaseModel):   #填寫想要販賣的小卡的資料(團名/成員名/價格(不可超過500元)/tag可以擺專輯或版本(通常會出好幾版本的專輯)/敘述就可以寫卡片的狀態
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


class User(BaseModel):   #賣家資訊
    username: str
    contact_id: str = Field(description="your phone/email or lind id")


@router.get("/{card_id}")   #這裡可以查想要的小卡(關鍵字q會放上建議填寫團名)
def read_card(
    card_id: Annotated[int, Path(title="The ID of the card to get", gt=0, le=45)],
    q: Annotated[str | None, Query(alias="group_name")] = None,
):
    results = {"card_id": card_id}
    if q:
        results.update({"q": q})
    return results


@router.post("/{card_id}")  #上架要賣的小卡的資料
def create_item(
    card_id: int, item: Annotated[Card, Body(embed=True)], user: User
):
    results = {"card_id": card_id, "item": item, "user": user}
    return results