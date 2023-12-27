from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .models.bookmark import BookmarkModelIn, BookmarkModelOut
app = FastAPI()
templates = Jinja2Templates("templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/bookmark", response_class=HTMLResponse)
async def create_bookmark(bookmark: BookmarkModelIn) -> BookmarkModelOut:
    return BookmarkModelOut(id=3, url=bookmark.url, tags=bookmark.tags)