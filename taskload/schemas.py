from pydantic import BaseModel

from taskload.models import TaskState


class TaskSchema(BaseModel):
    title: str
    description: str
    state: TaskState


class TaskPublic(BaseModel):
    id: int
    title: str
    description: str
    state: TaskState


class TaskList(BaseModel):
    tasks: list[TaskPublic]
