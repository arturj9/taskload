from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from taskload.database import get_session
from taskload.models import Task
from taskload.schemas import TaskList, TaskPublic, TaskSchema

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('/', response_model=TaskPublic)
def create_task(
    task: TaskSchema,
    session: Session = Depends(get_session),
):
    db_task: Task = Task(
        title=task.title,
        description=task.description,
        state=task.state,
    )
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.get('/', response_model=TaskList)
def list_task(
    session: Session = Depends(get_session),
    id: int = None
):
    query = select(Task)

    if id:
        query = query.filter(Task.id == id)

    tasks = session.scalars(query).all()

    return {'tasks': tasks}
