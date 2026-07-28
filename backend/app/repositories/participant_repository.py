from sqlalchemy.orm import Session

from app.models import Participant


class ParticipantRepository:
    def create(self, db: Session) -> Participant:
        participant = Participant()

        db.add(participant)
        db.commit()
        db.refresh(participant)

        return participant