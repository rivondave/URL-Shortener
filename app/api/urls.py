from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from fastapi import HTTPException

from app.models.url import URL

from app.schemas.url import (
    URLCreate,
    URLResponse
)

from app.core.utils import (
    generate_short_code
)

router = APIRouter(
    prefix="/urls",
    tags=["URLs"]
)

@router.post(
    "",
    response_model=URLResponse
)
def create_short_url(
    data: URLCreate,
    db: Session = Depends(get_db)
):

    if data.custom_alias:

        existing = (
            db.query(URL)
            .filter(
                URL.short_code
                == data.custom_alias
            )
            .first()
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Alias already exists"
            )

        short_code = data.custom_alias

    else:

        short_code = generate_short_code()

        while (
            db.query(URL)
            .filter(
                URL.short_code == short_code
            )
            .first()
        ):
            short_code = generate_short_code()

    new_url = URL(
        original_url=str(
            data.original_url
        ),
        short_code=short_code,
        expires_at=data.expires_at
    )

    db.add(new_url)

    db.commit()

    db.refresh(new_url)

    return new_url


@router.get(
    "/analytics/{short_code}"
)
def get_analytics(
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
            detail="URL not found"
        )

    return {
        "original_url": url.original_url,
        "short_code": url.short_code,
        "clicks": url.clicks,
        "created_at": url.created_at
    }


@router.get(
    "",
    response_model=list[URLResponse]
)
def get_urls(
    db: Session = Depends(get_db)
):

    return db.query(URL).all()