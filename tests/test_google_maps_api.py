from requests import Response

from utils.api import CoogleMapsApi


class TestCreatePlace:
    def test_create_new_place(self):
        print('\nМетод POST')
        result_post: Response = CoogleMapsApi.create_nem_pleace()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print('\nМетод GET')
        result_get: Response = CoogleMapsApi.get_nem_pleace(place_id)
        print(result_get)
