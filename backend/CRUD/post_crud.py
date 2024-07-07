# main.py
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from backend.databases import models, base
from backend.schemas import post_schemas


def create_post(post: post_schemas.PostInfo_create, db: Session = Depends(base.get_db)):
    post_data = post.dict()

    # 각 리스트 필드를 하나의 문자열로 변환
    for field in ["apply_online_url", "qualification", "preferred"]:
        if isinstance(post_data[field], list):
            post_data[field] = ", ".join(post_data[field])

    if post_data["qualification"] == "" and post_data["preferred"] == "":
        post_data["specific"] = False

    new_post = models.PostInfo(**post_data)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def read_post(db: Session, post_id: int):
    post = db.query(models.PostInfo).filter(models.PostInfo.post_id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
