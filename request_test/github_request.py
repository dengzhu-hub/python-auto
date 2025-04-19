import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()  # 加载.env文件
token = os.getenv("GITHUB_TOKEN")


try:
    response = requests.get('https://api.github.com/events')
    response.raise_for_status()  # 检查请求是否成功

    payload = {'username': 'jonas', 'password': 'asdmin', 'location': [
        'chong', 'qing'
    ]}
    response_param = requests.get(
        'https://api.github.com/events', params=payload)
    # print(response_param.url)  # 输出: 带参数的URL

    # 自定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    params = {
        'visibility': 'all',
        'per_page': 100
    }
    response = requests.get('https://api.github.com/user',
                            headers=headers, params=params)
    response.raise_for_status()
    # 获取响应内容
    print(f"响应状态码：{response.status_code}")

    print(f"响应头：{response.headers['Content-Type']}")

    payload_form = {'key1': 'value1', 'key2': 'value2'}
    response_post_form = requests.post(
        'https://httpbin.org/post',  json=payload_form)
    print("Respuesta POST (form):", response_post_form.json())
    # 获取响应内容
    # response.content: 返回 bytes 类型，适用于非文本内容（如图片、二进制文件）
    # response.text: 返回 string 类型，requests 会根据响应头或chardet库猜测编码进行解码
    print(f"响应文本 (前 100 字符): {response.text[:100]}...")

    try:
        json_data = response.json()
        print(f"响应 JSON 数据：{json_data}")
    except json.JSONDecodeError as err:
        print(f"JSON 解析错误：{err}")

    # 发送表单

    form_data = {'key1': 'value1', 'key2': 'value2'}
    response_post_form = requests.post(
        'https://httpbin.org/post', data=form_data)
    print("Respuesta POST (form):", response_post_form.json()['form'])

    # 发送 JSON 数据 (Content-Type: application/json)
    json_data = {'key1': 'value1', 'key2': 'value2'}
    headers = {
        'Content-Type': 'application/json',
        'X-Custom-Header': 'Custom Value'

    }
    response_post_json = requests.post(
        'https://httpbin.org/post', json=json_data, headers=headers)
    print("Respuesta POST (JSON):", response_post_json.json().get('json'))
    # 手动序列化
    json_data_str = {
        'username': 'jonas', 'password': 'asdmin'
    }
    response_post_json_str = requests.post(
        'https://httpbin.org/post',
        headers=headers,
        data=json.dumps(json_data_str)
    )

    # 文件上传 (multipart/form-data)
    url_upload = 'https://httpbin.org/post'
    try:
        with open('report.txt', 'rb') as f:
            files = {'file': ('report.txt', f, 'text/plain')}
            other_data = {'description': 'Monthly report'}
            response_upload = requests.post(
                url_upload, files=files, data=other_data)
    except FileNotFoundError:
        print("文件不存在")

    print("文件上传响应:", response_upload.json().get('files'))
    print("附带的表单数据:", response_upload.json().get('form'))

    response_put = requests.put(
        'https://httpbin.org/put', data={'key': 'new_value'})
    response_delete = requests.delete('https://httpbin.org/delete')
    response_head = requests.head('https://httpbin.org/get')  # 只获取响应头，不下载响应体
    response_options = requests.options(
        'https://httpbin.org/get')  # 获取服务器支持的 HTTP 方法

    print(f"PUT 状态码: {response_put.status_code}")
    print(f"DELETE 状态码: {response_delete.status_code}")
    print(
        f"HEAD 状态码: {response_head.status_code}, HEAD 响应头: {response_head.headers}")
    print(
        f"OPTIONS 状态码: {response_options.status_code}, 允许的方法: {response_options.headers.get('Allow')}")


except requests.exceptions.HTTPError as err:
    print(f"HTTP Error：{err}")
except requests.exceptions.ConnectionError as err:
    print(f"Connection Error: {err}")
