from utils.http_methods import HttpMethods

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"
post_resource = "/maps/api/place/add/json"
get_responce = "/maps/api/place/get/json"


class CoogleMapsApi:

    @staticmethod
    def create_nem_pleace():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "Ing": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone number": "(+91) 983 893 3937",
            "address": "29, sidelayout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_url = base_url + post_resource + key
        result_post = HttpMethods.post(post_url, json_for_create_new_place)

        print(result_post.text)
        return result_post

    @staticmethod
    def get_nem_pleace(place_id):
        get_url = base_url + get_responce + key + "&place_id=" + place_id
        result_get = HttpMethods.get(get_url)

        print(result_get.text)
        return result_get
