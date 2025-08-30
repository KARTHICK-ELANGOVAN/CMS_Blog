from sqlalchemy.orm import Session

from app import schemas
from app import models

def get_users(db: Session):
    return db.query(models.User).all()  # SELECT * FROM users;

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)  # create ORM object
    db.add(db_user)      # stage to insert
    db.commit()          # execute transaction
    db.refresh(db_user)  # reload from DB (gets ID)
    return db_user

def get_blogs(db: Session):
    return db.query(models.CMS_Blog_Main).all()

def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.CMS_Blog_Main(title=blog.title)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    print(db_blog.blog_id)
    return db_blog.blog_id

def get_blogContent(db: Session, blog_id: int):
    return db.query(models.CMS_Blog_Content_Header).filter(models.CMS_Blog_Content_Header.blog_id == blog_id).all()

def create_blogContent(db: Session, blog_content: schemas.BlogContentCreate, blog_id: int):
    db_blog_content = models.CMS_Blog_Content_Header(
        header=blog_content.header,
        header_font_size=blog_content.header_font_size,
        header_font_style=blog_content.header_font_style,
        header_font_color_code=blog_content.header_font_color_code,
        header_bold_flag=blog_content.header_bold_flag,
        blog_id=blog_id
    )
    print(blog_content.header_font_size)
    db.add(db_blog_content)
    db.commit()
    db.refresh(db_blog_content)
    return db_blog_content.content_header_id
