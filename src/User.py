# Represents a user with trips and friends.
class User:
    def __init__(self):
        self.friends = []
        self.trips = []

    def add_friend(self, friend):
        # Adds a friend to the user.
        self.friends.append(friend)

    def get_friends(self):
        # Returns the user's friends.
        return self.friends

    def add_trip(self, trip):
        # Adds a trip to the user's list of trips.
        self.trips.append(trip)

    def get_trips(self):
        # Returns the user's trips.
        return self.trips
