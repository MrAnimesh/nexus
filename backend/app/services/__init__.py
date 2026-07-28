from sqlalchemy.orm import Session

from app.models import Participant
from app.repositories.participant_repository import ParticipantRepository


class ParticipantService:
    def __init__(self, repository: ParticipantRepository) -> None:
        self.repository = repository

    def create_participant(self, db: Session) -> Participant:
        return self.repository.create(db)