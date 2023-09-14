from taskload.models import Task


def test_create_task(session):
    task = Task(title='Test Task', description='Test Desc', state='doing')

    session.add(task)
    session.commit()
    session.refresh(task)
