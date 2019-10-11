import os
import csv

from golfCourse import GolfCourse
from hole import Hole
from golfer import Golfer
from tournGolfer import TournGolfer
from tournament import Tournament
from round import Round
from golferRoundScores import GolferRoundScores

from golfTourDatabaseHelper import GolfTourDatabaseHelper


def main():
    """
    Algorithm:
    1.  Initialize the input and output file names
    2.  Initialize the database and table names for output
    3.  Call create_golf_courses function, passing in the the input
        file name, and retrieving the returned golf_course_list,
        a list of GolfCourse objects containing information for 5 golf courses
    4.  Call create_holes function, passing in the golf_course_holes_dict
        and retrieving the returned holes_list,
        a list of Hole objects containing information for 90 golf course holes
    5.  Call create_golfers function, passing in the input
        file name, and retrieving the returned golfer_list,
        a list of Golfer objects containing information for 30 golfers
    6.  Write out the class objects to files from:
        crate_golf_courses, create_holes, create_golfers
        ---------------------------------------------------------
    7.  Call create_tournaments function, passing in the input
        file name, and retrieving the returned tournament_list,
        a list of Tournament objects containing information for 15 tournaments
        and a tournament golfers dictionary, tournament_golfers_dict,
        whose key is the tourn_id and the value is the list of golfers
        playing in that tournament
    8.  Call create_rounds function, passing in the tournament_list from above,
        and retrieving the returned rounds_list,
        a list of Round objects containing information for 45 tournament rounds
    9.  Call create_tourn_golfers function, using the tournament_golfers_dict
        and the golfer_list from above, retrieving the returned tourn_golfers_list
        a list of TournGolfer objects containing information for 225 tournament golfers
    10. Write out the class objects to files from:
        create_tournaments, create_rounds, create_tourn_golfers
        ---------------------------------------------------------        
    11. Call create_golfer_scores function, passing in the round scores input
        file name, golfer_list returned from the create_golfers
        function, tournament_list returned from the create_tournaments
        function, and tourn_golfers_list returned from the
        create_tourn_golfers function, and retrieving the
        returned golfer_scores_list
    12. Write out the class objects to files from:
        create_golfer_scores
        ---------------------------------------------------------
    13. Remove the database, if it already exists
    14. Create a GolfTourDatabaseHelper object
    15. Use the GolfTourDatabaseHelper object to create
        the database and to create the tables.
    16. Use the GolfTourDatabaseHelper object to populate database tables
    17. Close the database connection
        ---------------------------------------------------------
    18. Write the following functions to query the database
        show_golf_course_last3_holes (database_name)
        show_tourn_scores_top5_Apex3 (database_name)
        show_golf_course_par5_holes (database_name)
        show_tournaments_for_golfer_Jo (database_name)
     """

    print("Wake Golf Tour Project 1")

    # 1. Initialize the input and output file names

    golf_courses_infile = "golfCoursesInput.csv"
    golfers_infile = "golfersInput.csv"
    tournaments_infile = "tournamentsInput.csv"
    golfer_scores_infile = "roundScoresInput.csv"

    golf_courses_file = "golfCourses.csv"
    holes_file = "holes.csv"
    golfers_file = "golfers.csv"
    tournaments_file = "tournaments.csv"
    tourn_golfers_file = "tournGolfers.csv"
    rounds_file = "rounds.csv"
    golfer_scores_file = "golferRoundScores.csv"

    # 2. Initialize the database and table names for output

    database_name = "WakeGolfTour.db"
    golf_courses_table = "GolfCourse"
    holes_table = "Hole"
    golfers_table = "Golfer"
    tournaments_table = "Tournament"
    tourn_golfers_table = "TournGolfer"
    rounds_table = "Round"
    golfer_scores_table = "GolferRoundScores"

    # 3. Call create_golf_courses function, passing in the input
    #    file name, and retrieving the returned golf_courses_list,
    #    a list of 5 golf course objects and the golf_course_holes_dict,
    #    containing information about the holes for each of the golf courses

    golf_course_list, golf_course_holes_dict = create_golf_courses(golf_courses_infile)

    # 4. Call create_holes function, passing in the golf_course_holes_dict
    #    and retrieving the returned holes_list,
    #    a list of Hole objects containing information for 90 golf course holes

    holes_list = create_holes(golf_course_holes_dict)

    # 5. Call create_golfers function, passing in the input
    #    file name, and retrieving the returned golfer_list,
    #    a list of 30 golfer objects

    golfer_list = create_golfers(golfers_infile)

    # 6. Write out the lists returned from the create functions:
    #    create_golf_courses, create_golfers, create_tournaments

    write_objs_to_file(golf_courses_file, golf_course_list)
    write_objs_to_file(holes_file, holes_list)
    write_objs_to_file(golfers_file, golfer_list)

    # 7. Call create_tournaments function, passing in the input
    #    file name and golf_course_list, retrieving the returned tournament_list,
    #    a list of 15 tournament objects, and a dictionary with the tourn_id as the key
    #    and a list of golfers for that tournament as the value

    tournament_list, tourn_golfers_dict = create_tournaments(tournaments_infile, golf_course_list)

    # 8. Call create_rounds function, passing in the input
    #    file name and the tournament_list, retrieving the returned rounds_list,
    #    a list of Round objects

    rounds_list = create_rounds(tournament_list)

    # 9. Call create_tourn_golfers function, using tourn_golfers_dict
    #    and the golfers_list, retrieving the returned tourn_golfers_list,
    #    a list of TournGolfer objects

    tourn_golfers_list = create_tourn_golfers(tourn_golfers_dict, golfer_list)

    # 10. Write out the lists returned from the create functions:
    #    create_holes, create_rounds, create_tourn_golfers

    write_objs_to_file(tournaments_file, tournament_list)
    write_objs_to_file(rounds_file, rounds_list)
    write_objs_to_file(tourn_golfers_file, tourn_golfers_list)
    
    # 11. Call create_golfer_scores function, passing in the
    #     golfer_scores_list returned from the read_golfer_scores
    #     function, golfers_list returned from the read_golfers
    #     function, tourns_list returned from the create_tournaments
    #     function, rounds_list returned from the create_rounds
    #     function, and the tourn_golfers_list returned from the
    #     create_tourn_golfers function, and retrieving the
    #     returned golfer_scores_list

    golfer_scores_list = create_golfer_scores(golfer_scores_infile,
                                              golfer_list,
                                              tournament_list,
                                              rounds_list,
                                              tourn_golfers_list)

    # 12. Write out the class objects to a file from:
    #     create_golfer_scores

    write_objs_to_file(golfer_scores_file, golfer_scores_list)
    print()
    
    # 13. Remove the database, if it already exists

    if os.path.exists(database_name):
        os.remove(database_name)

    # 14. Create a GolfTourDatabaseHelper object

    db_helper = GolfTourDatabaseHelper(database_name)

    # 15. Use the GolfTourDatabaseHelper object to create
    #     the database and to create the tables.

    db_helper.create_database()

    # 16. Use the GolfTourDatabaseHelper object to populate database tables

    db_helper.save_to_database(golf_courses_table, golf_courses_file)
    db_helper.save_to_database(holes_table, holes_file)
    db_helper.save_to_database(golfers_table, golfers_file)
    db_helper.save_to_database(tournaments_table, tournaments_file)
    db_helper.save_to_database(tourn_golfers_table, tourn_golfers_file)
    db_helper.save_to_database(rounds_table, rounds_file)
    db_helper.save_to_database(golfer_scores_table, golfer_scores_file)

    # 17. Close the database connection

    db_helper.close_connection()

    # 18. Write the following functions to query the database

    show_golf_course_last3_holes(database_name)
    show_tourn_scores_top5_Apex3(database_name)
    show_golf_course_par5_holes(database_name)
    show_tournaments_for_golfer_Jo(database_name)
    
    # Add the call to your own function here:
    show_my_query(database_name)
     
    
def create_golf_courses(filename):
    """
    Each line of input contains:
    golf_course_name, par_h1, par_h2, ..., par_h18

    where golf_course_name is the name of the golf course and each
          par_h# is a par value for the hole #.
    
    Note: string input needs to be stripped of any whitespace
             integer strings need to be changed to ints 

    Create a new GolfCourse object containing 
        golf_course_id, golf_course_name, total_par
          
    Return a list,  where each element is a GolfCourse object
    """

    print("\nGolf Course List: golf_course_list\n")

    # 1. Create an empty list called golf_course_list that will contain
    #    GolfCourse objects whose data comes from the input file

    golf_course_list = []

    # 2. Create an empty dictionary called golf_course_holes_dict
    #    whose key is the golf_course_id and the value is a tuple
    #    containing hole_number and par_value
    
    golf_course_holes_dict = dict()

    # 3. Initialize the golf_course_id to 1

    golf_course_id = 1

    # 4. Use a try/except block to capture a File Not Found Error

    try:
        # a. Open the input_file object for reading the input file

        input_file = open(filename, 'r')

        # b. Call the csv.reader function, passing in the input file
        #    and capturing the CSV file contents.

        file_lines = csv.reader(input_file)

        # c. Create a list from the file contents: courses_list

        courses_list = list(file_lines)

        # d. Create an outer loop to read each golf course in
        #    courses_list

        for golf_course in courses_list:

            # Outer Loop
            # 1. The first element (golf course name) is stripped
            #    of whitespace.

            golf_course_name = golf_course[0].strip()

            # 2. Create an inner loop to traverse the 18 hole
            #    par values using the range function

            total_par = 0
            holes = []
            for i in range(1,19):
                # Inner Loop
                # a. Convert the string hole par values to ints
                par = int(golf_course[i])

                # b. Add value to total par
                total_par = total_par + par

                # c. Append hole_num and par to list for dictionary
                holes.append((i, par))

            # 3. Add entry for this golf course's holes to the golf_course_holes_dict
            golf_course_holes_dict[golf_course_id] = holes

            # 4. Create a new GolfCourse object, call it golf_course,
            #    passing in golf_course_id, golf_course_name, and total_par

            golf_course = GolfCourse(golf_course_id, golf_course_name, total_par)

            # 5. Append the golf_course object to the golf_course_list

            golf_course_list.append(golf_course)

            # 6. Increment the golf_course_id

            golf_course_id = golf_course_id + 1

        # e. Close input_file object

        input_file.close()

    except IOError:
        print("File Not Found Error.")

    # 5. Print the golf_course_list objects to the console

    for gc in golf_course_list:
        print(gc)

    # 6. Return the golf_course_list and golf_course_holes_dict

    return golf_course_list, golf_course_holes_dict
    
    
def create_holes(golf_course_holes_dict):
    """
    Use the dictionary created in the create_golf_courses function
    to create a list of Hole objects. The dictionary has golf_course_id as the key,
    and a list of 18 tuples containing (hole_num, par_value) as the value
        Each entry will have:
         golf_course_id: [(hole_num, par_value), 
                          (hole_num, par_value), ..., 
                          (hole_num, par_value)]
                                 
    Create a Hole object for each hole_num and par_value
    containing - 
        hole_id, golf_course_id, hole_num, and par_value

    Return a list,  where each element is a Hole object
                                 
    """
    print("\nThe Hole object list:\n")
    
    #  Create an empty list called holes_list
    holes_list = []

    # initialize hole_id
    hole_id = 1

    # outer loop reads key(1) into golf_course_id, and puts the value into hole_info
    for golf_course_id, hole_info in golf_course_holes_dict.items():

        # inner loop through hole_info to get hole_num and par_value
        for info in hole_info:
            hole_num = info[0]
            par_value = info[1]

            # create a new Hole object passing in hole_id, golf_course_id, hole_num, par_value
            hole_obj = Hole(hole_id, golf_course_id, hole_num, par_value)

            # append hole object to the hole_list
            holes_list.append(hole_obj)

            # increment hole_id
            hole_id += 1

    # print the holes_list objects to the console
    for ob in holes_list:
        print(ob)

    return holes_list


def create_golfers(filename):
    """
    Each line of input contains:
    golfer_name, golfer_birthdate

    where golfer_name is the name of the golfer and
          golfer_birthdate is the day the golfer was born.

    Note: string input needs to be stripped of any whitespace

    Create a Golfer object from each line in the input file:
    containing -
    golfer_id, golfer_name, golfer_birthdate

    A list is returned, where each element is a Golfer object

    """
    print ("\nThe Golfer object list:\n")

    # Create an empty list called golfer_list
    golfer_list = []

    # use try/except block to capture a File Not Found Error
    try:
        # open the input_file for reading the input file
        input_file = open(filename, 'r')

        # call the csv.reader function
        file2_lines = csv.reader(input_file)

        # create a list from file contents
        golfer_id_list = list(file2_lines)

        # initialize golfer_id
        golfer_id = 1;

        # create loop to read each golfer in golfer_id_list
        for golfer in golfer_id_list:

            # string input stripped of any whitespace
            golfer_name = golfer[0].strip()
            golfer_birthdate = golfer[1].strip()
            golfer_city = golfer[2].strip()

            # create Golfer object, passing golfer_id, golfer_name, golfer_birthdate
            golfer_obj = Golfer(golfer_id, golfer_name, golfer_birthdate, golfer_city)

            # append golfer object to golfer_list
            golfer_list.append(golfer_obj)

            # increment golfer_id
            golfer_id += 1

        # close input_file object
        input_file.close()

    except IOError:
        print("File Not Found Error.")

    for gl in golfer_list:
        print(gl)

    return golfer_list


def create_tournaments(filename, golf_course_list):
    """
    The tournamentsInput.csv has two different record types in the file.
    Hint: Open the file and see how it is organized.
    The first record type has

    golf_course_name, tourn_name, start_date, num_rounds, num_golfers

    where golf_course_name is the name of the golf course,
          tourn_name is the name of the tournament,
          start_date is the first day of the tournament,
          num_rounds is the number of rounds played in this tournament, and
          num_golfers is the number of golfers playing in this tournament

    The second record type is just a single golfer name.
    The number of these records is specified by the num_golfers field from the first record type
        golfer1_name
        golfer2_name
        ...
        golfer15_name

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Create a Tournament object 
    containing - 
        golfer_id, golfer_name, golfer_birthdate

    Create dictionary entry value for this tourn_id_key, 
        the value is a list to be filled in with the golfer names 
        as they are read from the input file. 
   
    Return the tournament_list and tourn_golfers_dict
    """
    print("\nThe Tournament object list:\n")
    
    # Create a lookup table dictionary for mapping the golf_course_name to the golf_course_id using the passed in golf_course_list
    golf_course_name_to_id = dict()

    # Traverse the GolfCourse objects in the golf_course_list - course holds a GolfCourse object
    for course in golf_course_list:
        # Code fills dictionary, where the key is golf_course_name, and the value is the golf_course_id
        # Both items are taken from the GolfCourse object using the getters.
        golf_course_name_to_id[course.get_course_name()] = course.get_course_id()

    # Create an empty list that will be filled with tournament objects
    tournament_list = []

    # Create an empty dictionary that will be filled in with the tournament id as the key and the list of golfers as the value
    tourn_golfers_dict = dict()

    # Initialize the tourn_id to 1
    tourn_id = 1

    # Initialize the tourn_id_key to 0
    tourn_id_key = 0

    # Use a try/except block to capture a File Not Found Error
    try:
        # Open the input_file object for reading the input file
        input_file = open(filename, 'r')

        # Call the csv.reader function, passing in the input file and capturing the CSV file contents.
        file2_lines = csv.reader(input_file)

        # Create a list from the file contents: tourn_list
        tournament_input_list = list(file2_lines)

        # Create a loop to traverse the tournament_input_list
        for tourn_info in tournament_input_list:
            # Check the length of tourn_info; if length is greater than one, then process the tournament information
            if len(tourn_info) > 1:
                # string input stripped of any whitespace
                golf_course_name = tourn_info[0].strip()
                tourn_name = tourn_info[1].strip()
                start_date = tourn_info[2].strip()
                num_rounds = tourn_info[3].strip()
                num_golfers = tourn_info[4].strip()

                # Get golf_course_id from lookup dictionary created above
                golf_course_id = golf_course_name_to_id[golf_course_name]

                # Create a new Tournament object, call it tournament, passing in tourn_id, tourn_name, golf_course_id,
                # start_date, num_rounds, and num_golfers
                tournament = Tournament(tourn_id, tourn_name, golf_course_id, start_date, num_rounds, num_golfers)

                # Append the tournament object to the tournament_list
                tournament_list.append(tournament)

                # Set tourn_id_key to tourn_id
                tourn_id_key = tourn_id

                # Create dictionary entry value for this tourn_id_key, the value is an empty list to be filled in later
                # with the golfer names as they are read from the input file
                tourn_golfers_dict[tourn_id_key] = []

                # Increment the tourn_id
                tourn_id += 1

            # Else the length of tourn_info is one, add it to the tourn_golfers_dict value list. It will be used
            # later in the create_tourn_golfers method.
            else:
                # Get the golfer name from the tourn_info stripping whitespace
                golfer_name = tourn_info[0].strip()

                # Add the golfer name to the tourn_golfers_dict value
                tourn_golfers_dict[tourn_id_key].append(golfer_name)

        # Close input_file object
        input_file.close()

    except IOError:
        print("File Not Found Error.")

    # Print the tournament_list objects to the console
    for item in tournament_list:
        print(item)
    
    return tournament_list, tourn_golfers_dict


def create_rounds(tournament_list):
    """
    Use the tournament_list object list, that was
    returned from the create_tournaments function, which
    contains 15 Tournament objects with the following
    instance variables:

    tourn_id, tourn_name, golf_course_id, start_date,
    num_rounds, num_golfers, golfers...

    Create num_rounds Round objects from every
    Tournament object element in tournament_list:
    Add in the following as instance variables values

    round_id, tourn_id, day

    A list is returned, where each element is a Round object

    """
    print("\nThe Round object list\n")

    # Create an empty list that will be filled with Round objects whose data comes from the parameter tournament_list
    rounds_list = []

    # Initialize round_id
    round_id = 1

    # Create an outer looper to traverse the input tournament_list, where the loop variable "tourn" will contain
    # one of the Tournament objects in tournament_list at each loop iteration
    for tourn in tournament_list:
        # Get the number_rounds and tourn_id from Tournament object, tourn, and initialize num_rounds to number_rounds -
        # this will be decremented below to find the correct day for the Round object being built
        tourn_id = tourn.get_tourn_id()
        number_rounds = tourn.get_num_rounds()
        num_rounds = int(number_rounds)

        # Create an inner loop to run number_round times using the range function, where the loop variable 'r' keeps
        # the number of Rounds being created
        for r in range(int(number_rounds)):
            # Check the value of num_rounds to determine the day value of this Round object.
            if int(num_rounds) == 4:
                day = "Thu"
            elif int(num_rounds) == 3:
                day = "Fri"
            elif int(num_rounds) == 2:
                day = "Sat"
            elif int(num_rounds) == 1:
                day = "Sun"

            # Decrement the num_rounds counter
            num_rounds -= 1

            # Create a Round object call it round passing in round_id, tourn_id, and day
            round = Round(round_id, tourn_id, day)

            # Append the Round object to the rounds_list
            rounds_list.append(round)

            # Increment the round_id
            round_id += 1

    # Print the round objects to the console
    for item in rounds_list:
        print(item)

    return rounds_list


def create_tourn_golfers(tourn_golfers_dict,  golfer_list):
    """
    Use the tourn_golfers_dict, that was
    returned from the create_tournaments function, which contains
    entries with the key being the tourn_id, and the value is a list following format:
    of golfer_names

    Use the golfers_list object list parameter, that was
    returned from the create_golfers function, which
    contains 30 Golfer objects with the following instance
    variables:

    golfer_id, golfer_name, golfer_birthdate

    Create a TournGolfer object from every golfer_name listed
    in the tourn_golfers_dict.
    Add in the following as instance variables values -

        tourn_golfer_id, tourn_id, golfer_id

    A list is returned, where each element is a TournGolfer object
    
    """

    print("\nThe TournGolfer object list\n")

    # Create a lookup dictionary (golfer_name_to_id) for golfer_name to golfer_id
    golfer_name_to_id = dict()
    for golfer in golfer_list:
        golfer_name_to_id[golfer.get_golfer_name()] = golfer.get_golfer_id()

    # Create an empty list that will be filled with TournGolfer objects whose data comes from the tournaments_list
    # parameter, and object list parameter, golfers_list
    tourn_golfers_list = []

    # Initialize the tourn_golfer_id
    tourn_golfer_id = 1

    # Create an outer loop to traverse the input tourn_golfers_dict, whose key will contain the tournament_id, and the
    # value, 'golfer_name_list', will be the list of golfer names for that tournament
    for tournament_id, golfer_name_list in tourn_golfers_dict.items():

        # Create an inner loop to traverse the golfer_name_list, where the loop variable 'golfer_name' will contain one
        # of the golfer names for the tournament
        for golfer_name in golfer_name_list:

            # Get golfer_id from (golfer_name_to_id) lookup dictionary
            golfer_id = golfer_name_to_id[golfer_name]

            # Create a TournGolfer object call it tourn_golfer, passing in tourn_golfer_id, tourn_id (from the dict key),
            # and golfer_id
            tourn_golfer = TournGolfer(tourn_golfer_id, tournament_id, golfer_id)

            # Append the TournGolfer object to the tourn_golfers_list
            tourn_golfers_list.append(tourn_golfer)

            # Increment the tourn_golfer_id
            tourn_golfer_id += 1

    # Print the tourn_golfers_list object to console
    for item in tourn_golfers_list:
        print(item)

    return tourn_golfers_list

    
def create_golfer_scores(filename, golfer_list, tournament_list,
                         rounds_list, tourn_golfers_list):
    """
    Create GolferRoundScores objects from data in the input file,
    and using previously created object lists to convert names to ids.

    Each line of input contains:
        golfer_name, tourn_name, day, score_h1, score_h2, ..., score_h18

    where golfer_name is the name of the golfer,
          tourn_name is the name of the tournament,
          day is the round day,
          and each score_h# is the golfer's score for that hole

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Use the golfers_list parameter, that was
    returned from the create_golfers function, with the
    following instance variables:

        golfer_id, golfer_name, golfer_birthdate

    Use the tourns_list parameter, that was
    returned from the create_tournaments function, with the
    following instance variables:

        tourn_id, tournament_name, golf_course_id, start_date,
        num_rounds, and num_golfers

    Use the rounds_list object list parameter, that was
    returned from the create_rounds function, with the
    following instance variables:

        round_id, tourn_id, day

    Use the tourn_golfers_list parameter, that was
    returned from the create_tourn_golfers function, with the
    following instance variables:

        tourn_golfers_id, tourn_id, golfer_id

    Create a GolferRoundScores object from every entry in the
    golfer_scores_list:  Add in the following as instance
    variables values:

        golfer_scores_id, tourn_golfer_id, round_id, total_round_score,
        and a list of scores (score_h1, score_h2, ..., score_h18)

    A list is returned, where each element is a GolferRoundScore object

    """

    print("\nThe GolferRoundScores object list\n")

    # Create a lookup dictionary (golfer_name_to_id) for associating a golfer_name to golfer_id
    golfer_name_to_id = dict()
    for golfer in golfer_list:
        golfer_name_to_id[golfer.get_golfer_name()] = golfer.get_golfer_id()

    # Create a lookup dictionary (tourn_name_to_id) for associating tourn_name to tourn_id
    tourn_name_to_id = dict()
    for tournament in tournament_list:
        tourn_name_to_id[tournament.get_tourn_name()] = tournament.get_tourn_id()

    # Create an empty list that will be filled in with GolferRoundScore objects whose data comes from the input file
    # and each of the object list parameters: golfers_list, tourns_list, rounds_list, tourn_golfers_list
    round_scores_list = []

    # Initialize the golfer_scores_id
    golfer_scores_id = 1

    # Use a try/except block to capture a File Not Found Error
    try:
        # Open the input file object for reading the input file
        input_file = open(filename, 'r')

        # Call the csv.reader function, passing in the input file and capturing the CSV file contents.
        file3_lines = csv.reader(input_file)

        # Create a list from the file contents: 'golfer_scores_list'
        golfer_scores_list = list(file3_lines)

        # Create an outer loop to read each set of scores in 'golfer_scores_list'
        for scores in golfer_scores_list:

            # Get the golfer_name, tourn_name, and day from the first three elements, stripping whitespace.
            golfer_name = scores[0].strip()
            tourn_name = scores[1].strip()
            day = scores[2].strip()

            # The rest of the elements (using slice scores[3:]) are converted to a list of ints - scores_list.
            # Use python 'map' function to convert the object returned from the map to a list.
            scores_list = []
            scores_list = list(map(int, scores[3:]))

            # Get the golfer_id using the golfer_name_to_id
            golfer_id = golfer_name_to_id[golfer_name]

            # Get the tourn_id using the tourn_name_to_id
            tourn_id = tourn_name_to_id[tourn_name]

            # Call the helper functions to get round_id, and the tourn_golfer_id
            tourn_golfer_id = get_tourn_golfer_id(tourn_golfers_list, tourn_id, golfer_id)
            round_id = get_round_id(rounds_list, tourn_id, day)

            # Set the total_round_score by summing the scores_list
            total_round_score = sum(scores_list)

            # Create a new GolferRoundScores object, call it golfer_scores, passing in golfer_scores_id,
            # tourn_golfer_id, round_id, total_round_score, and the scores list
            golfer_scores = GolferRoundScores(golfer_scores_id, tourn_golfer_id, round_id, total_round_score, scores_list)

            # Append the GolferRoundScores object to the round_scores_list
            round_scores_list.append(golfer_scores)

            # Increment the golfer_scores_id
            golfer_scores_id += 1

        # Close input_file object
        input_file.close()

    except IOError:
        print("File Not Found Error.")

    # Print the round_scores_list objects to the console.
    for item in round_scores_list:
        print(item)

    # Return the round_scores_list
    return round_scores_list


def get_tourn_golfer_id(tourn_golfers_list, tourn_id, golfer_id):
    """
    Helper function to get the tourn_golfer_id
    based on the specified tourn_id and golfer_id
    """

    for tourn_golfer in tourn_golfers_list:
        if tourn_golfer.get_golfer_id() == golfer_id:
            if tourn_golfer.get_tourn_id() == tourn_id:
                return tourn_golfer.get_tourn_golfer_id()

    # tg not found - just return 0
    return 0


def get_round_id(rounds_list, tourn_id, tourn_day):
    """
    Helper function to get the round_id
    based on the specified tourn_id and tourn_day

    """

    for round_id in rounds_list:
        if round_id.get_tourn_id() == tourn_id:
            if round_id.get_day() == tourn_day:
                return round_id.get_round_id()

    # tg not found - just return 0
    return 0


def write_objs_to_file(filename, object_list):
    """
    This function takes a nested_list as input and writes it
    out to a csv file, where each line is a inner list

    """
    # 1. Open the output file object for writing

    output_file = open(filename, 'w')

    # 2. Create a loop to traverse the object_list parameter,
    #    where the loop variable is each object in the list:

    for obj in object_list:
        # Loop:
        # a. Set a str_obj string variable to the result of
        #    converting 'object' to a string using the
        #    __str__ method of the output file.  This can be
        #    accomplished by passing the object into the
        #    str() function.

        str_obj = str(obj)

        # b. Add a new line character to the end of the
        #     str_obj string

        str_obj += '\n'

        # c. Use the write method of the output file object
        #    to write the str_obj string to the output file,

        output_file.write(str_obj)

    # 3. Close the output file

    output_file.close()


def show_golf_course_last3_holes(database_name):
    """
    Show a list of golf course names with the total par
    and the hole number and par for the last 3 holes
    """

    print("\nLast 3 holes, of each golf course\n")

    # Get a cursor for the connection

    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query

    sql = '''
        select course_name, course_total_par,
              hole_number, hole_par
        from GolfCourse join Hole
        on course_id = hole_course_id
        where hole_number > 15
    '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()
    
    # Close the cursor and the database connection
    c.close()
    database_connection.close()


def show_tourn_scores_top5_Apex3(database_name):
    """
    Show the total tournament scores for the top
    five golfers, who played the 'Apex 3' tournament
    """

    print("\nTotal Scores For Top 5 Golfers in Apex 3 Tournament\n")

    # Get a cursor for the connection

    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query

    sql = '''
        select golfer_name, tourn_name, sum (grs_total_score) as total
           from GolferRoundScores
              join TournGolfer on
                   grs_tourn_golfer_id = tg_id
              join Golfer on
                   tg_golfer_id = golfer_id
              join Tournament on
                   tg_tourn_id = tourn_id
           where tourn_name = 'Apex 3'
           group by grs_tourn_golfer_id
           order by tourn_name, total
           limit 5
    '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()
    
    # Close the cursor and the database connection
    c.close()
    database_connection.close()


def show_golf_course_par5_holes(database_name):
    """
    Show a list of golf course names with the total par
    and the hole number and par for each hole where the
    par is equal to 5: 
    """
    
    print("\nShow the Par 5 Hole Numbers For Each Golf Course\n")
    
    # Get a cursor for the connection
    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query
    sql = '''
    select course_name, course_total_par, hole_number, hole_par
        from GolfCourse join Hole
        on course_id = hole_course_id
        where hole_par = '5'
    '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()

    # Close the cursor and the database connection
    c.close()
    database_connection.close()


def show_tournaments_for_golfer_Jo(database_name):
    """
    Show a list of tournaments and golfer names played by golfers
    whose name begins with Jo: 
    """

    print("\nTournaments Played by Golfer's Whose Name Begins With Jo\n")
    
    # Get a cursor for the connection
    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query
    sql = '''
    select golfer_name, tourn_name
        from TournGolfer
            join Tournament on 
                tg_tourn_id = tourn_id
            join Golfer on 
                tg_golfer_id = golfer_id
        where golfer_name like 'Jo%'
        order by golfer_name
    '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()

    # Close the cursor and the database connection
    c.close()
    database_connection.close()

    
def show_my_query(database_name):
    """
    Show data from the golf tour database
    """

    print("\nData from my query\n")
    
    # Get a cursor for the connection
    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query
    sql = '''
        select tourn_name, golfer_name, golfer_city
                from Tournament
                join TournGolfer on tourn_id = tg_tourn_id
                join Golfer on  tg_golfer_id = golfer_id
                where golfer_city != 'Raleigh' and tourn_name = 'Raleigh 1'
    '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()

    # Close the cursor and the database connection
    c.close()
    database_connection.close()


main()
