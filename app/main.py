from fastapi import FastAPI

from datetime import datetime

from app.api.urls import (
    router as urls_router
)

from app.models.url import URL

from app.core.database import (
    Base,
    engine
)

from sqlalchemy import inspect

from fastapi import Depends
from fastapi import HTTPException

from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.url import URL

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="URL Shortener API",
    version="1.0.0"
)

app.include_router(urls_router)


@app.get("/")
def root():

    return {
        "message": "URL Shortener Running"
    }

@app.get("/{short_code}")
def redirect_url(
    short_code: str,
    db: Session = Depends(get_db)
):

    url = (
        db.query(URL)
        .filter(
            URL.short_code == short_code
        )
        .first()
    )

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )
    
    if (
        url.expires_at
        and
        datetime.utcnow()
        > url.expires_at
    ):
        raise HTTPException(
            status_code=410,
            detail="Link has expired"
        )

    url.clicks += 1

    db.commit()

    return RedirectResponse(
        url=url.original_url
    )
