from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.participant_repository import ParticipantRepository
from app.schemas.participant import ParticipantResponse
from app.services.participant_service import ParticipantService


router = APIRouter(
    prefix="/participants",
    tags=["Participants"],
)

repository = ParticipantRepository()
service = ParticipantService(repository)


@router.post(
    "",
    response_model=ParticipantResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_participant(
    db: Annotated[Session, Depends(get_db)],
) -> ParticipantResponse:
    return service.create_participant(db)