from time import timezone
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from app.database import Base
from datetime import datetime
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class CMS_Blog_Main(Base):
    __tablename__ = "cms_blog_main"

    blog_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    #author_id = Column(Integer, ForeignKey("users.id"))
    #publish_flag = Column(Boolean, default=False)
    #last_published_date = Column(DateTime, default=lambda: datetime.now(tz=IST))
    #image_url = Column(String)


class CMS_Blog_Content_Header(Base):
    __tablename__ = "cms_blog_content_header"

    content_header_id = Column(Integer, primary_key=True, index=True)
    blog_id = Column(Integer, ForeignKey("cms_blog_main.blog_id"))
    header = Column(String)
    header_font_size = Column(String)
    header_font_style = Column(String)
    header_font_color_code = Column(String)
    header_bold_flag = Column(Boolean, default=False)
