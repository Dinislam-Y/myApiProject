from utils.http_methods import HttpMethods
from utils.data import TestDataJson

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"
post_resource = "/maps/api/place/add/json"  # Ресурс метода Post
get_resource = "/maps/api/place/get/json"  # Ресурс метода Get
put_resource = "/maps/api/place/update/json"  # Ресурс метода Put
testDataJson = TestDataJson.testDataJson


class CoogleMapsApi:

    # Метод для создания новой локации
    @staticmethod
    def create_new_place():
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, testDataJson)
        print(result_post.text)
        return result_post

    # Метод для проверки новой локации
    @staticmethod
    def get_new_place(place_id):
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    # Метод для проверки новой локации
    @staticmethod
    def put_new_place(place_id):
        get_url = base_url + put_resource + key + "&place_id=" + place_id
        print(get_url)
        result_put = HttpMethods.put(get_url, place_id)
        print(result_put.text)
        return result_put
