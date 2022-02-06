from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class viewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        """Correct car data - post a new car"""
        self.car_data = {"make": "BMW", "model": "M8"}
        self.response = self.client.post(
            '/cars/',
            self.car_data,
            format='json'
        )

        """Incorect car data (model does not exist in external API) - post a new car"""
        self.car_data_2 = {"make": "BMW", "model": "do not exist"}
        self.response_2 = self.client.post(
            "/cars/",
            self.car_data_2,
            format='json'
        )

        """Correct rate data - post a new rate"""
        self.rate_data = {"car_id": 1, "rate": 5}
        self.response_3 = self.client.post(
            "/rate/",
            self.rate_data,
            format="json"
        )
    
        """Incorrect rate data (to big rate) - post a new rate"""
        self.rate_data_2 = {"car_id": 1, "rate": 6}
        self.response_4 = self.client.post(
            "/rate/",
            self.rate_data_2,
            format="json"
        )

    def test_api_can_get_car(self):
        response = self.client.get("/cars/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_popular_car(self):
        response = self.client.get('/popular/', format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_create_a_car(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_create_a_not_exist_car(self):
        self.assertEqual(self.response_2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_post_rate(self):
        self.assertEqual(self.response_3.status_code, status.HTTP_201_CREATED)

    def test_api_can_post_bad_rate(self):
        self.assertEqual(self.response_4.status_code, status.HTTP_400_BAD_REQUEST)
