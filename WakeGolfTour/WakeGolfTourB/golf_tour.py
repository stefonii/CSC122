import csv
import pdb

from golfCourse import GolfCourse
from hole import Hole
from golfer import Golfer
from tournGolfer import TournGolfer
from tournament import Tournament
from round import Round


def main():
    """
    1.  Initialize the input and output file names
    2.  Initialize the database and table names for output
    3.  Call create_golf_courses function, passing in the the input
        file name, and retrieving the returned golf_course_list,
        a list of GolfCourse objects containing information for 5 
        golf courses and the returned golf_course_holes_dict which 
        has the golf_course_id as the key, and the value is a list 
        of 18 tuples containing (hole_num, par_value).
    4.  Call create_holes function, passing in the 
        golf_course_holes_dict and retrieving the returned 
        holes_list, a list of Hole objects containing information 
        for 90 (5*18) golf course holes
    5.  Call create_golfers function, passing in the input file name, 
        and retrieving the returned golfer_list, a list of Golfer 
        objects containing information for 30 golfers
    6.  Write out the class objects to files from:
        create_golf_courses, create_holes, create_golfers
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
     """

    print("Wake Golf Tour Project 1")

    # 1. Initialize the input and output file names

    golf_courses_infile = "golfCoursesInput.csv"
    golfers_infile = "golfersInput.csv"
    tournaments_infile = "tournamentsInput.csv"

    golf_courses_file = "golfCourses.csv"
    holes_file = "holes.csv"
    golfers_file = "golfers.csv"
    tournaments_file = "tournaments.csv"
    tourn_golfers_file = "tournGolfers.csv"
    rounds_file = "rounds.csv"

    # 2. Initialize the database and table names for output

    golf_courses_table = "GolfCourse"
    holes_table = "Hole"
    golfers_table = "Golfer"
    tournaments_table = "Tournament"
    tourn_golfers_table = "TournGolfer"
    rounds_table = "Round"

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

            # 2. Add entry for this golf course's holes to the golf_course_holes_dict
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
                  golfer_birthdate is the date the golfer was born.

    Note: string input needs to be stripped of any whitespace

    Create a Golfer object from each line in the input file:
    containing - 
        golfer_id, golfer_name, golfer_birthdate

    Return a list,  where each element is a Golfer object
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

            # create Golfer object, passing golfer_id, golfer_name, golfer_birthdate
            golfer_obj = Golfer(golfer_id, golfer_name, golfer_birthdate)

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
    entries with the key being the tourn_id, and the value is a list of golfer_names

    Use the golfers_list object list parameter, that was returned from the 
    create_golfers function, which contains 30 Golfer objects with 
    the following instance  variables:

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


main()
