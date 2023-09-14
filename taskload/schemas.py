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


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TaskState | None = None


class Message(BaseModel):
    detail: str
