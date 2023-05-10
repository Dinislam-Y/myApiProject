from requests import Response

from utils.api import CoogleMapsApi


class TestCreatePlace:
    def test_api(self):
        print('\nМетод POST')
        result_post: Response = CoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print('\nМетод GET POST')
        result_get: Response = CoogleMapsApi.get_new_place(place_id)

        print('\nМетод PUT')
        result_put: Response = CoogleMapsApi.put_new_place(place_id)

        print('\nМетод GET PUT')
        result_get: Response = CoogleMapsApi.get_new_place(place_id)
