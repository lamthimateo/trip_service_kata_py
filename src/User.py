class User:
    def __init__(self):
        self.friends = []
        self.trips = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def get_friends(self):
        return self.friends

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_trips(self):
        return self.trips
