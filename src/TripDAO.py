from DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException


# DAO class to find trips for a user. Raises exception during unit tests.
class TripDAO:
    @staticmethod
    def find_trips_by_user(user):
        # Raises an exception to prevent actual data access during unit tests.
        raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked during a unit test.")
