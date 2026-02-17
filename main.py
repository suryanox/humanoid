import logging

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from humanoid.models import InitiateInteractionResponse, InteractionResponse
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


@router.get("/initiate_interaction", response_model=InitiateInteractionResponse)
def initiate_interaction():
    return service.initiate_interaction()


@router.get("/interact/{session_id}", response_model=InteractionResponse)
def interact(session_id: str):
    return service.interact(session_id)

app.include_router(router)
