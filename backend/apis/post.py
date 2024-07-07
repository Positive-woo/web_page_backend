# main.py
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from backend.databases import models, base
from backend.schemas import post_schemas
from backend.CRUD import post_crud

post_router = APIRouter()

models.Base.metadata.create_all(bind=base.engine)


@post_router.post("/create/", response_model=post_schemas.PostInfo_read)
def create_post_route(
    post: post_schemas.PostInfo_create, db: Session = Depends(base.get_db)
):
    try:
        new_post = post_crud.create_post(post, db)
        if new_post is None:
            raise HTTPException(status_code=400, detail="Post creation failed")
        return new_post
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@post_router.get("/posts/{post_id}", response_model=post_schemas.PostInfo_read)
def read_post_route(post_id: int, db: Session = Depends(base.get_db)):
    try:
        return post_crud.read_post(db, post_id)
    except HTTPException as he:
        # CRUD 함수에서 발생한 HTTP 예외를 그대로 전달
        raise he
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
