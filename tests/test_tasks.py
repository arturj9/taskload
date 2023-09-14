from taskload.models import Task


def test_create_task(client):
    response = client.post(
        '/tasks/',
        json={
            'title': 'Test Task',
            'description': 'Test Desc',
            'state': 'doing',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'title': 'Test Task',
        'description': 'Test Desc',
        'state': 'doing',
    }


def test_list_task(session, client):
    task1 = Task(title='Test Task1', description='Test Desc1', state='doing')
    task2 = Task(title='Test Task2', description='Test Desc2', state='done')
    session.add(task1)
    session.add(task2)
    session.commit()

    response = client.get('/tasks/')

    assert len(response.json()['tasks']) == 2


def test_list_taks_filter_id(session, client):
    task1 = Task(title='Test Task1', description='Test Desc1', state='doing')
    task2 = Task(title='Test Task2', description='Test Desc2', state='done')
    session.add(task1)
    session.add(task2)
    session.commit()

    response = client.get(f'/tasks/?id={task2.id}')

    assert response.json()['tasks'][0]['id'] == task2.id


def test_patch_task_error(client):
    response = client.patch('/tasks/10', json={})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Task not found.'}


def test_patch_task(session, client):
    task = Task(title='Test Task', description='Test Desc', state='doing')
    session.add(task)
    session.commit()

    response = client.patch(
        f'/tasks/{task.id}',
        json={'title': 'teste!'},
    )
    assert response.status_code == 200
    assert response.json()['title'] == 'teste!'


def test_delete_task(session, client):

    task = Task(title='Test Task', description='Test Desc', state='doing')
    session.add(task)
    session.commit()

    response = client.delete(f'/tasks/{task.id}')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Task has been deleted successfully.'}


def test_delete_task_error(client):
    response = client.delete('/tasks/10')

    assert response.status_code == 404
    assert response.json() == {'detail': 'Task not found.'}
