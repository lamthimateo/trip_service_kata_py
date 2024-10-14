from DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException


class TripDAO:
    @staticmethod
    def find_trips_by_user(user):  # Rename the method to use snake_case
        raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked on a unit test.")
