class TournGolfer:
    """
    TournGolfer object derived from data in the tournamentInput.csv

    Instance variables:
        tourn_golfer_id    a unique id for this tourn_golfer (to be used as a primary key when stored in the database)
        tourn_id           the id of the tournament played by the golfer
        golfer_id          the id of the golfer playing in the tournament

    """

    def __init__(self, tourn_golfer_id, t_id, g_id):
        """
        Constructor of class TournGolfer
        """
        self.__tourn_golfer_id = tourn_golfer_id
        self.__tourn_id = t_id
        self.__golfer_id = g_id

    def get_tourn_golfer_id(self):
        """
        Return the tourn_golfer_id to the caller
        """
        return self.__tourn_golfer_id

    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    def get_golfer_id(self):
        """
        return the golfer_id to the caller
        """
        return self.__golfer_id

    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_str = "{0},{1},{2}".format(self.__tourn_golfer_id, self.__tourn_id, self.__golfer_id)
        return csv_str
