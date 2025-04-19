import requests
import json

base_url = 'https://jsonplaceholder.typicode.com'
endpoint = '/posts'
headers = {
    'Content-Type': 'application/json',
    'X-Custom-Header': 'Custom Value',


}
post_data = {
    "userId": 1,
    "title": "我的自动化测试帖子",
    "body": "这是使用 Python requests 库发送的自动化测试创建的帖子。"
}

response = requests.post(base_url + endpoint, json=post_data, headers=headers)
print(f"请求成功，状态码: {response.status_code}")
assert response.status_code == 201, f"请求失败，状态码: {response.status_code}"
print(f"创建成功")

print(f"响应体：")
print(response.json())

# assert
response_json = response.json()
assert response_json['userId'] == post_data['userId']
assert response_json['title'] == post_data['title']
assert response_json['body'] == post_data['body']
assert 'id' in response_json
print("响应体数据验证通过")

# response = requests.get(base_url + endpoint)
# assert response.status_code == 200
# assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
# assert response.json() == json.loads(response.text)
# data = response.json()
# print(f"请求成功，状态码: {response.status_code}")
# print(f"请求结果: {data}")


# get specific post by id
endpoint = '/posts/{post_id}'
exiting_post_id = 1

response = requests.get(base_url + endpoint.format(post_id=exiting_post_id))

print(f"请求成功，状态码: {response.status_code}")

assert response.status_code == 200, f"expected status code 200, got {response.status_code}"
print(f"获取 {exiting_post_id} 成功。")

print(response.json())

response_json = response.json()
assert 'userId' in response_json and response_json['userId'] == 1
assert 'id' in response_json and response_json['id'] == exiting_post_id
print(f"post {exiting_post_id} 数据验证通过")


# 测试获取一个不存在的 Post (通常会返回 404 Not Found)

non_existent_post_id = 999
response_not_found = requests.get(
    base_url + endpoint.format(post_id=non_existent_post_id))
print(
    f"Status Code for non-existent Post {non_existent_post_id}: {response_not_found.status_code}")

assert response_not_found.status_code == 404, f"expected status code 404, got {response_not_found.status_code}"
print("获取不存在的 Post 返回 404 验证通过")


# 验证更新 Post API (PUT)
endpoint = '/posts/{post_id}'
exiting_post_id = 2

updated_post_data = {

    "title": "更新后的标题",
    "body": "更新后的内容"
}
response = requests.put(
    base_url + endpoint.format(post_id=exiting_post_id, json=updated_post_data)
)
print(f"Status  code: {response.status_code}")

assert response.status_code == 200, f"expected status code 200, got {response.status_code}"
print(f"Post {exiting_post_id} 更新请求已发送")

# 现在，执行 GET 请求获取更新后的帖子
response_get = requests.get(
    base_url + endpoint.format(post_id=exiting_post_id))
print(
    f"Status code for updated Post {exiting_post_id}: {response_get.status_code}")
assert response_get.status_code == 200, f"expected status code 200, got {response_get.status_code}"

# 验证 GET 请求的响应体，确保数据已更新
update_response_json = response_get.json()

assert update_response_json['id'] == exiting_post_id

print(f"Post {exiting_post_id} 更新验证通过")
