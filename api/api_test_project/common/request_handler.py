import requests
from logger import logger


class RequestHandler:
    def __init__(self):
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        logger.info(f"请求地址：{url}")
        logger.info(f"请求方法：{method}")
        logger.info(f"请求参数: {kwargs}")
        res = self.session.request(method, url, **kwargs)
        logger.info(f"响应状态码：{res.status_code}")
        logger.info(f"相应内容：{res.text}")
        return res
