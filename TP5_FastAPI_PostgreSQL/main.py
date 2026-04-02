from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal

# Create tables
try:
    models.Base.metadata.create_all(bind=engine)
except Exception as error:
    print(f"Database initialization warning: {error}")

app = FastAPI()

# -------------------
# Pydantic Models
# -------------------

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


# -------------------
# Database Dependency
# -------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


# -------------------
# Create Question
# -------------------

@app.post("/questions/")
def create_question(question: QuestionBase, db: db_dependency):

    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)

    db.commit()

    return {"message": "Question created successfully ✅"}


# -------------------
# Get Question
# -------------------

@app.get("/questions/{question_id}")
def read_question(question_id: int, db: db_dependency):

    result = db.query(models.Questions).filter(
        models.Questions.id == question_id
    ).first()

    if not result:
        raise HTTPException(status_code=404, detail="Question not found")

    return result


# -------------------
# Get Choices
# -------------------

@app.get("/choices/{question_id}")
def read_choices(question_id: int, db: db_dependency):

    result = db.query(models.Choices).filter(
        models.Choices.question_id == question_id
    ).all()

    if not result:
        raise HTTPException(status_code=404, detail="Choices not found")

    return result