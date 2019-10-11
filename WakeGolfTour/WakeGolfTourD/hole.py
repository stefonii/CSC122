class Hole:
    """
    Hole object derived from data in the golfCoursesInput.csv

    Instance variables:
        hole_id         a unique id for this hole (to be used as a primary key when stored in the database)
        course_id      the id of the golf course where this hole is played
        hole_num        the number of the hole (1-18)
        par             the par value for this hole (3,4, or 5)
    """

    def __init__(self, hole_id, c_id, h_num, p):
        """
        constructor of class Hole
        """
        self.__hole_id = hole_id
        self.__course_id = c_id
        self.__hole_num = h_num
        self.__par = p

    def get_hole_id(self): #hole_id
        """
        return the hole_id to the caller
        """
        return self.__hole_id

    def get_course_id(self): #course_id
        """
        return the course_id to the caller
        """
        return self.__course_id

    def get_hole_num(self): #hole_num
        """
        return the hole_num to the caller
        """
        return self.__hole_num

    def get_par(self): #par
        """
        return the hole par to the caller
        """
        return self.__par

    def __str__(self):
        """
        create a comma-delimiter string
        of the instance variable values
        """
        csv_str = "{0},{1},{2},{3}".format(self.__hole_id, self.__course_id, self.__hole_num, self.__par)
        return csv_str
