from main import server

def test_devops_request():
    name = "Juan Perez"
    response = server.test_client().post("/DevOps", json={
        "message": "This is a test",
        "to": name,
        "from": "R1ita Asturia",
        "timeToLifeSec": 45
    })

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert response.json['message'] == 'Hello {0} your message will be send'.format(name)
