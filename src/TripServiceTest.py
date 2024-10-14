import unittest
from unittest.mock import patch

from Trip import Trip
from TripService import TripService
from User import User
from UserNotLoggedInException import UserNotLoggedInException


class TripServiceTest(unittest.TestCase):

    def setUp(self):
        self.trip_service = TripService()
        self.user = User()

    @patch('UserSession.get_instance')
    def test_should_throw_exception_when_user_is_not_logged_in(self, mock_session):
        mock_session.return_value.get_logged_user.return_value = None
        with self.assertRaises(UserNotLoggedInException):
            self.trip_service.get_trips_by_user(self.user)

    @patch('UserSession.get_instance')
    @patch('TripDAO.find_trips_by_user')
    def test_should_return_trips_when_users_are_friends(self, mock_find_trips, mock_session):
        friend = User()
        trip = Trip()

        mock_session.return_value.get_logged_user.return_value = self.user
        self.user.add_friend(friend)
        mock_find_trips.return_value = [trip]

        result = self.trip_service.get_trips_by_user(friend)
        self.assertEqual(result, [trip])

    @patch('UserSession.get_instance')
    def test_should_return_empty_list_when_users_are_not_friends(self, mock_session):
        mock_session.return_value.get_logged_user.return_value = self.user
        not_friend = User()

        result = self.trip_service.get_trips_by_user(not_friend)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
