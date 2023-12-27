from pydantic import BaseModel, HttpUrl

class BookmarkModel(BaseModel):
    url: HttpUrl
    tags: str | None


class BookmarkModelIn(BookmarkModel):
    pass

class BookmarkModelOut(BookmarkModel):
    id: int