import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
print(response.json())


data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
print(response.json())