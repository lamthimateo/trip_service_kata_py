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
    @patch('TripService.TripDAO.find_trips_by_user')  # Updated method name to snake_case
    def test_should_return_trips_when_users_are_friends(self, mock_find_trips, mock_get_logged_user):
        friend = User()
        trip = Trip()

        # Mock the session to return the logged-in user
        mock_get_logged_user.return_value = self.user
        # Mock the TripDAO to return a list of trips
        self.user.add_friend(friend)
        mock_find_trips.return_value = [trip]

        # Now call the TripService method
        result = self.trip_service.get_trips_by_user(friend)
        # Assert that the result is the list of trips
        self.assertEqual(result, [trip])

    @patch.object(UserSession, 'get_logged_user')
    def test_should_return_empty_list_when_users_are_not_friends(self, mock_get_logged_user):
        mock_get_logged_user.return_value = self.user
        not_friend = User()

        result = self.trip_service.get_trips_by_user(not_friend)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
