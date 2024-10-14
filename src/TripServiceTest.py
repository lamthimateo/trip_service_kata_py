import unittest
from unittest.mock import patch
from TripService import TripService
from User import User
from Trip import Trip
from UserSession import UserSession
from TripDAO import TripDAO
from UserNotLoggedInException import UserNotLoggedInException


class TripServiceTest(unittest.TestCase):

    def setUp(self):
        self.trip_service = TripService()
        self.user = User()

    @patch.object(UserSession, 'get_logged_user')
    @patch('TripService.TripDAO.find_trips_by_user')  # Correct patch
    def test_should_return_trips_when_users_are_friends(self, mock_find_trips, mock_get_logged_user):
        friend = User()  # This line and others must be indented correctly
        trip = Trip()

        mock_get_logged_user.return_value = self.user
        self.user.add_friend(friend)
        mock_find_trips.return_value = [trip]

        result = self.trip_service.get_trips_by_user(friend)
        self.assertEqual(result, [trip])

    @patch.object(UserSession, 'get_logged_user')
    def test_should_return_empty_list_when_users_are_not_friends(self, mock_get_logged_user):
        mock_get_logged_user.return_value = self.user
        not_friend = User()

        result = self.trip_service.get_trips_by_user(not_friend)
        self.assertEqual(result, [])

    @patch.object(UserSession, 'get_logged_user')
    @patch('TripService.TripDAO.find_trips_by_user')  # Ensure correct method is patched
    def test_should_not_return_trips_if_users_have_not_traveled_together(self, mock_find_trips, mock_get_logged_user):
        friend = User()
        trip = Trip()

        mock_get_logged_user.return_value = self.user
        self.user.add_friend(friend)
        mock_find_trips.side_effect = [[], [trip]]  # No trips for user, trips for friend

        result = self.trip_service.get_trips_by_user(friend)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
