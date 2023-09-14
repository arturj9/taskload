from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from taskload.database import get_session
from taskload.models import Task
from taskload.schemas import (
    Message,
    TaskList,
    TaskPublic,
    TaskSchema,
    TaskUpdate,
)

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('/', status_code=201, response_model=TaskPublic)
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


@router.get('/', status_code=200, response_model=TaskList)
def list_task(session: Session = Depends(get_session), id: int = None):
    query = select(Task)

    if id:
        query = query.filter(Task.id == id)

    tasks = session.scalars(query).all()

    return {'tasks': tasks}


@router.patch('/{task_id}', response_model=TaskPublic)
def patch_task(
    task_id: int, task: TaskUpdate, session: Session = Depends(get_session)
):
    db_task = session.scalar(select(Task).where(Task.id == task_id))

    if not db_task:
        raise HTTPException(status_code=404, detail='Task not found.')

    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.delete('/{task_id}', status_code=200, response_model=Message)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.scalar(select(Task).where(Task.id == task_id))

    if not task:
        raise HTTPException(status_code=404, detail='Task not found.')

    session.delete(task)
    session.commit()

    return {'detail': 'Task has been deleted successfully.'}
