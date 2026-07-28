from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app.api.participant import router as participant_router


app = FastAPI(
    title="Nexus API",
    version="0.1.0",
)

app.include_router(participant_router)



@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/database")
def database_health_check(
    db: Annotated[Session, Depends(get_db)],) -> dict[str, str]:
    db.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "connected",
    }