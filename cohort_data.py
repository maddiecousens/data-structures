def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """

    houses = set()

    # Code goes here
    with open(filename) as cohort_data:
        for student in cohort_data:
            student_info = student.split("|")
            if student_info[2]:
                houses.add(student_info[2])
    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Put ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...], 
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    # Code goes here
    with open(filename) as cohort_data:
        for student in cohort_data:
            student = student.rstrip()
            student_info = student.split('|')
            if student_info[2]:
                #print (student_info[-1] == "Winter 2016")
                if student_info[-1] == "Winter 2016":
                    winter_16.append(" ".join(student_info[0:2]))
                    #print " ".join(student_info[0:2])
                    #print winter_16
                elif student_info[-1] == "Spring 2016":
                    spring_16.append(" ".join(student_info[0:2]))
                elif student_info[-1] == "Summer 2016":
                    summer_16.append(" ".join(student_info[0:2]))
                elif student_info[-1] == "Fall 2015":
                    fall_15.append(" ".join(student_info[0:2]))
            else:
                ghosts.append(" ".join(student_info[0:2]))
        all_students = [sorted(winter_16), sorted(spring_16), sorted(summer_16),
                        sorted(fall_15), sorted(ghosts)] 
        # print sorted(winter_16)
        # print '*'*80
        # print sorted(summer_16)
        # print '*'*80
        # print sorted(spring_16)
        # print '*'*80
        # print sorted(fall_15)
        # print all_students


    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.


    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Return all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    # Code goes here
    with open(filename) as cohort_data:
        for student in cohort_data:
            student = student.rstrip()
            student_info = student.split('|')
            if student_info[2]:
                #print (student_info[-1] == "Winter 2016")
                if student_info[2] == "Gryffindor":
                    gryffindor.append(student_info[1])
                    #print " ".join(student_info[0:2])
                    #print winter_16
                elif student_info[2] == "Hufflepuff":
                    hufflepuff.append(student_info[1])
                elif student_info[2] == "Slytherin":
                    slytherin.append(student_info[1])
                elif student_info[2] == "Dumbledore's Army":
                    dumbledores_army.append(student_info[1])
                elif student_info[2] == "Ravenclaw":
                    ravenclaw.append(student_info[1])
                elif student_info[-1] == "I":
                    instructors.append(student_info[1])
                else:
                    ghosts.append(student_info[1])
        all_students = [sorted(gryffindor), sorted(hufflepuff), sorted(slytherin),
                        sorted(dumbledores_army), sorted(ravenclaw), sorted(ghosts), sorted(instructors)] 
    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

#print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
