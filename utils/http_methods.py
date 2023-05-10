import requests


class HttpMethods:
    headers = {'Content-Type': 'application'}
    cookie = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.get(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.get(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.get(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
