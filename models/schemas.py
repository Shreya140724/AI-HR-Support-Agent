from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    username: str
    password: str

class QueryRequest(BaseModel):
    query: str

class LearnRequest(BaseModel):
    question: str
    correct_answer: str