from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr  

class UserCreate(UserBase):
    pass  

class UserOut(UserBase):
    id: int  
    class Config:
        orm_mode = True 



class BlogBase(BaseModel):
    title: str

class BlogCreate(BlogBase):
    pass

class BlogOut(BlogBase):
    id: int

    class Config:
        orm_mode = True 


#BlogContentCreate

class BlogContentBase(BaseModel):
    blog_id: int
    header: str
    header_font_size: str
    header_font_style: str
    header_font_color_code: str
    header_bold_flag: bool

class BlogContentCreate(BlogContentBase):
    pass

class BlogContentOut(BlogContentBase):
    id: int

    class Config:
        orm_mode = True 
