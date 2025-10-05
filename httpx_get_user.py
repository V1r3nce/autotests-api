import httpx
import httpx
from tools.fakers import fake

create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()

print(f"Create response: {create_user_response_data}")
print(f"Status code: {create_user_response.status_code}")

login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")

info_headers = {'Authorization': f'Bearer {login_response_data['token']['accessToken']}'}
info_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", headers=info_headers)
info_response_data = info_response.json()

print(f"Login response: {info_response_data}")
print(f"Status code: {info_response.status_code}")