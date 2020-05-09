from .consts import CONDITIONS

class Dock:
    """
    A Dock to hold bikes. Each dock resides in 
    """
    conditions = CONDITIONS

    def __init__(self, id, bike = None):
        """
        Parameters
        ----------
        id: [int >= 0] the id no. for the station.

        bike: [Bike | None] The Bike or None value to occupy this dock.
        """
        self.id = id
        self.bike = None
        self.condition = self.conditions[0]
        self.log = []
    
    def check_in(self, bike, time, station):
        """
        Check a bike into this dock.

        Parameters
        ----------
        bike: [Bike] The bike parking at this station.

        time: [int] The time in minutes since the simulation began.

        station: [int] The station id corresponding to where this dock resides.
        """
        self.bike = bike
        self.log.append({
            'bike_id': self.bike.id,
            'trip_id': self.bike._uses, # This line may mess us up. not sure how to track yet
            'end_time': time
        })

    def check_out(self, time, station):
        """
        Check a bike out of this dock.

        Parameters
        ----------
        time: [int] The time in minutes since the simulation began.

        station: [int] The station id corresponding to where this dock resides.
        """
        self.bike.ride()

        self.log.append({
            'bike_id': self.bike.id,
            'trip_id': self.bike._uses, # This line may mess us up. not sure how to track yet
            'start_time': time
        })

        self.bike = None
    

