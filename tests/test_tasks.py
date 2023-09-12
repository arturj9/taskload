def test_create_todo(client):
    response = client.post(
        '/tasks/',
        json={
            'title': 'Test Task',
            'description': 'Test Desc',
            'state': 'doing',
        },
    )
    assert response.json() == {
        'id': 1,
        'title': 'Test Task',
        'description': 'Test Desc',
        'state': 'doing',
    }

    print(response.json())
