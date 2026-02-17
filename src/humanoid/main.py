import logging

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from humanoid.models import InitiateInteractionResponse, InteractionResponse, InitiateInteractionRequest, \
    InteractionRequest
from humanoid.middleware import ErrorHandlingMiddleware
from humanoid import service

logging.basicConfig(level=logging.INFO)
app = FastAPI()

app.add_middleware(ErrorHandlingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api/v1")


@router.get("/health")
def health_check():
    return {"status": "healthy"}


@router.post("/initiate_interaction", response_model=InitiateInteractionResponse)
async def initiate_interaction(request: InitiateInteractionRequest):
    return await service.initiate_interaction(request)


@router.post("/interact/{session_id}", response_model=InteractionResponse)
async def interact(session_id: str, request: InteractionRequest):
    return await service.interact(session_id, request)

app.include_router(router)
