from .conftest import client


def test_signup_patient():
    response = client.post(
        "/signup/patient",
        json={
            "email": "patient1@mail.com",
            "password": "password"
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "patient1@mail.com"

    #Duplicate patient
    response = client.post(
        "/signup/patient",
        json={
            "email": "patient1@mail.com",
            "password": "password2"
        }
    )

    assert response.status_code == 409

def test_login_patient():
    response = client.post(
        "/token",
        data={
            "username": "patient1@mail.com", 
            "password": "password"},
        headers={"content-type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == 200
    data = response.json()
    access_token = data["access_token"]

    response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "patient1@mail.com"

    response = client.post(
        "/token",
        data={
            "username": "patient1@mail.com", 
            "password": "passwort2"},
        headers={"content-type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == 400

def test_signup_therapist():
    response = client.post(
        "/signup/therapist",
        json={
            "email": "therapist1@mail.com",
            "password": "password"
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "therapist1@mail.com"

    # Duplicate therapist
    response = client.post(
        "/signup/therapist",
        json={
            "email": "therapist1@mail.com",
            "password": "password2"
        }
    )

    assert response.status_code == 409

def test_login_therapist():
    response = client.post(
        "/token",
        data={
            "username": "therapist1@mail.com", 
            "password": "password"},
        headers={"content-type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == 200
    data = response.json()
    access_token = data["access_token"]

    response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "therapist1@mail.com"

    response = client.post(
        "/token",
        data={
            "username": "therapist1@mail.com", 
            "password": "passwort2"},
        headers={"content-type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == 400

def test_get_users():
    response = client.get(
        "/users"
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    
    
