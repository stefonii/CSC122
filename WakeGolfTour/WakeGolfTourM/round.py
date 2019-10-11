class Round:
    """
    Round object derived from data in the tournamentInput.csv

    Instance variables:
        round_id        a unique id for this round (to be used as a primary key when stored in the database)
        tourn_id        the id of the tournament for this round
        day             the day that the round was played ('Thu', 'Fri', 'Sat', 'Sun')
    """

    def __init__(self, round_id, tour_id, day):
        """
        constructor of the class Round
        """
        self.__round_id = round_id
        self.__tourn_id = tour_id
        self.__day = day

    def get_round_id(self):
        """
        return the round_id to the caller
        """
        return self.__round_id

    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    def get_day(self):
        """
        return the day to the caller
        """
        return self.__day

    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_str = "{0},{1},{2}".format(self.__round_id, self.__tourn_id, self.__day)
        return csv_str

