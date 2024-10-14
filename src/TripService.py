from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:

    def get_trips_by_user(self, user):
        logged_in_user = UserSession.get_instance().get_logged_user()
        self._validate_logged_in_user(logged_in_user)

        if self._is_friend(logged_in_user, user) and self._have_traveled_together(logged_in_user, user):
            return TripDAO.find_trips_by_user(user)
        else:
            return []

    def _validate_logged_in_user(self, user):
        if user is None:
            raise UserNotLoggedInException()

    def _is_friend(self, logged_in_user, user):
        return user in logged_in_user.get_friends()

    def _have_traveled_together(self, logged_in_user, user):
        user_trips = TripDAO.find_trips_by_user(logged_in_user)
        return any(trip in user_trips for trip in TripDAO.find_trips_by_user(user))
