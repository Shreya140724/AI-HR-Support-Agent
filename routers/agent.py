from fastapi import APIRouter
from models.schemas import QueryRequest, LearnRequest
from services.agent_service import process_query
from services.rag_service import add_to_memory

router = APIRouter()

@router.post("/query")
async def query_agent(request: QueryRequest):

 result = process_query(
    request.query
)

 return result

@router.post("/learn")
async def learn(request: LearnRequest):


 add_to_memory(
    request.question,
    request.correct_answer
)

 return {
    "message":
    "Successfully learned! Agent will remember this."
}
