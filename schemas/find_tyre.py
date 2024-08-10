from pydantic import BaseModel


class MaskTyre(BaseModel):
    diameter: int
    width: int
    height: int
    season: list[str]
    thorn: bool
    wrh_list: list[int]
    brand_list: list[str]



