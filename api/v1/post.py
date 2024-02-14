from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import repository.post
from database.postupdate import PostUpdate
from infrastructure.mysql import get_db
from schema.database.post import PostCreate

router = APIRouter(
    tags=["post"],
    prefix="/posts"
)


@router.get("", tags=["Post"])
def list_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = repository.post.lists(db, skip=skip, limit=limit)
    return posts


@router.post("", tags=["Post"])
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return repository.post.create(db=db, post=post)


@router.delete("/{post_id}", tags=["Post"])
def delete(post_id: int, db: Session = Depends(get_db)):
    post = repository.post.get_post(db, post_id)
    return repository.post.delete(db=db, post=post)


@router.patch("/{post_id}", tags=["Post"])
def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(get_db)):
    existing_post = repository.post.get_post(db, post_id)
    if existing_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post = repository.post.patch_post(db, post_id, post_update)
    return updated_post

@router.get("/{post_id}", tags=["Post"])
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = repository.post.get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post