from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


# Service class for retrieving trips for a user.
class TripService:
    def get_trips_by_user(self, user):
        # Gets the trips for a user if they are friends with the logged-in user.
        logged_in_user = UserSession.get_instance().get_logged_user()
        self._validate_logged_in_user(logged_in_user)

        if self._is_friend(logged_in_user, user) and self._have_traveled_together(logged_in_user, user):
            return TripDAO.find_trips_by_user(user)
        return []

    def _validate_logged_in_user(self, user):
        # Validates that the user is logged in.
        if user is None:
            raise UserNotLoggedInException()

    def _is_friend(self, logged_in_user, user):
        # Checks if the logged-in user is a friend of the target user.
        return user in logged_in_user.get_friends()

    def _have_traveled_together(self, logged_in_user, user):
        # Verifies if the users have traveled together.
        user_trips = TripDAO.find_trips_by_user(logged_in_user)
        return any(trip in user_trips for trip in TripDAO.find_trips_by_user(user))
