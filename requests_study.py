import os
import certifi
import requests
import json
from pathlib import Path

# 1. GET请求
# response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
# print(response.status_code)  # 输出: 200

# data = response.json()

# 2. 使用Path对象创建目录
# base_dir = Path(__file__).parent  # 获取当前文件所在目录
# target_dir = base_dir / 'pokemon_data'  # 创建目标目录路径
# target_dir.mkdir(parents=True, exist_ok=True)  # 创建目录，如果不存在则创建
# file_path = target_dir / 'ditto.json'  # 创建文件路径


# with file_path.open('w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
# print(f"数据已保存到 {file_path}")

# print(response.json())  # 输出: {'name': 'ditto', 'height': 3, ...}


def get_pokemon_info(name):
    """
    获取指定宝可梦的信息。
    :param name: 宝可梦的名称
    :return: 宝可梦的信息
    """
    base_url = 'https://pokeapi.co/api/v2'
    endpoint = f'/pokemon/{name}'
    url = base_url + endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None


pokenmon_name = 'pikachu'
response = get_pokemon_info(pokenmon_name)
# print(response)
if response:
    print(f"宝可梦名称: {response['name']}")
    print(f"宝可梦高度: {response['height']}")
    print(f"宝可梦体重: {response['weight']}")
    print(f"宝可梦类型: {[type['type']['name'] for type in response['types']]}")


url = 'https://httpbin.org/basic-auth/jonas/asdmin'
# 2. POST请求
data = {'user': 'jonas'}
# response = requests.post(url, data=data)
# print(response.status_code)  # 输出: 200
# 输出: {'args': {}, 'data': '', 'files': {}, 'form': {'key': 'value'}, ...}
# form_data = response.json().get('form', {})
# print(form_data)  # 输出: {'user': 'jonas'}
# print(response.text)  # 输出: 原始响应文本
# print(response.content)  # 输出: 原始响应内容
# print(response.headers)  # 输出: 响应头信息
# print(response.cookies)  # 输出: 响应中的Cookies
print(response.url)  # 输出: 请求的URL
# print(response.history)  # 输出: 请求的历史记录
# print(response.encoding)  # 输出: 响应的编码方式
# print(response.elapsed)  # 输出: 请求耗时
# print(response.raise_for_status())  # 输出: None，如果请求失败则抛出异常
# print(response.json())  # 输出: 响应的JSON数据
# print(response.ok)  # 输出: True，如果请求成功则为True
# print(response.status_code)  # 输出: 响应的状态码
# print(response.request)  # 输出: 请求对象
# print(response.request.headers)  # 输出: 请求头信息

# 3. 处理SSL证书验证
response = requests.get(
    'https://httpbin.org/basic-auth/jonas/asdmin')  # 禁用SSL证书验证

# response = requests.get('https://example.com', verify=certifi.where())  # 使用certifi提供的证书
# print(response.text)  # 输出: 响应文本

# proxies

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
}

# 4. 设置请求超时

url = 'https://httpbin.org/get'
url_back = 'https://jsonplaceholder.typicode.com/posts/1'
url_delay = 'https://httpbin.org/delay/6'
try:
    response = requests.get(url_delay, timeout=3)  # 设置超时时间为5秒
    response.raise_for_status()
    print(response.text)  # 输出: 响应文本
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.HTTPError as err:
    print(f"Http error: {err.response.status_code} - {err}")

except requests.exceptions.ConnectionError as err:
    print(f"Connection error: {err}")
except requests.exceptions.RequestException as err:
    print(f"unknown error: {err}")
