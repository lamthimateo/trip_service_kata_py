import unittest

from src.TripService import TripService
from src.User import User
from src.UserNotLoggedInException import UserNotLoggedInException


class TestTripService(unittest.TestCase):

    def setUp(self):
        self.trip_service = TripService()
        self.logged_in_user = User()
        self.target_user = User()

    def test_user_not_logged_in_raises_exception(self):
        with self.assertRaises(UserNotLoggedInException):
            self.trip_service.get_trips_by_user(None, self.target_user)

    def test_no_friends_returns_empty_trip_list(self):
        result = self.trip_service.get_trips_by_user(self.logged_in_user, self.target_user)
        self.assertEqual(result, [])

    def test_friends_with_no_trips_returns_empty_trip_list(self):
        self.logged_in_user.addFriend(self.target_user)
        result = self.trip
