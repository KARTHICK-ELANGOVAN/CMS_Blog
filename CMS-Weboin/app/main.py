from fastapi import FastAPI, HTTPException, Depends, Request,Form
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from app import schemas, services, models

from app.database import SessionLocal, engine, get_db, create_table

app = FastAPI()

create_table()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_users(request: Request, db: Session = Depends(get_db)):
    users = services.get_users(db)
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

'''@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)   # inserts new user'''

@app.post("/add_user")
def add_user(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    user = schemas.UserCreate(name=name, email=email)
    services.create_user(db, user)
    return RedirectResponse("/", status_code=303)

@app.get("/blog", response_class=HTMLResponse)
def read_blogs(request: Request, db: Session = Depends(get_db)):
    blogs = services.get_blogs(db)
    if blogs is None:
        blogs="blog not exist"
    return templates.TemplateResponse("cms_blog_index.html", {"request": request, "blogs":blogs})

@app.post("/add_blog")
def add_blog(request: Request,
    title: str = Form(...),
    db: Session = Depends(get_db)
):
    blog = schemas.BlogCreate(title=title)
    blog_id =services.create_blog(db, blog)

    #return RedirectResponse("/blog", status_code=303)
    return RedirectResponse(f"/blog/{blog_id}", status_code=303)


#create blog content and show

@app.get("/blog/{blog_id}", response_class=HTMLResponse)
def read_blogContent(blog_id: int, request: Request, db: Session = Depends(get_db)):
    blog = services.get_blogContent(db, blog_id)
    if blog is None:
        blog="blog not exist"
    return templates.TemplateResponse("cms_blog_content.html", {"request": request, "blog":blog, "blog_id": blog_id})

@app.post("/add_blogContent")
def add_blogContent(request: Request,
    blog_id: int = Form(...),
    header: str = Form(...),
    header_font_size: str = Form(...),
    header_font_style: str = Form(...),
    header_font_color_code: str = Form(...),
    header_bold_flag: bool = Form(False),
    db: Session = Depends(get_db)
):
    print(f"blog_id: {blog_id},{header}, {header_font_size},{header_font_style}, {header_font_color_code}, {header_bold_flag}")
    blog_header = schemas.BlogContentCreate(
        blog_id=blog_id,
        header=header,
        header_font_size=header_font_size,
        header_font_style=header_font_style,
        header_font_color_code=header_font_color_code,
        header_bold_flag=header_bold_flag
    )
    services.create_blogContent(db, blog_header, blog_id)

    #return RedirectResponse("/blog", status_code=303)
    return RedirectResponse(f"/blog/{blog_id}", status_code=303)
