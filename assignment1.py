"""
Replace the contents of this module docstring with your own details
Name: Kyaw Soe Naing
Date started: 29/11/2019
GitHub URL: https://github.com/Ezra2952/assignment-01-Ezra2952
"""
from operator import itemgetter

print("Movies To Watch 1.0 - by Kyaw Soe Naing")
MENU = """Menu:
L - List movies
A - Add new movies
W - Watch a movie
Q - Quit
"""
# Read all data from movies.csv file
DATAFILE = "movies.csv"
Database = open(DATAFILE, "r")
read_list = Database.readlines()
# all data from csv file is stored in movies = [] as nested list
movies = []
Database.close()
print("{:d} movies loaded".format(len(read_list)))
# split into years and than movies name
for line in read_list:
    line = line.strip()
    inline = line.split(",")
    inline[1] = int(inline[1])
    # sort line into years and than movies name
    movies.append(inline)
    movies.sort(key=itemgetter(1, 0))


# Main Function including other many functions
def main():
    user_input = menu()
    while user_input != "q":
        if user_input == "l":
            all_movies()
            user_input = menu()
        elif user_input == "a":
            add_movies()
            user_input = menu()
        elif user_input == "w":
            watch_list()
            user_input = menu()
        else:
            print("Invalid menu choice")
            user_input = menu()
# Write all changes data to csv file
    Database = open(DATAFILE, "w")
    for movie in movies:
        movie[1] = str(movie[1])
        text = ",".join(movie)
        text = text + "\n"
        Database.write(text)

    Database.close()

    print("{} movies saved to {}".format(len(movies), DATAFILE))
    print("Have a nice day :)")


# ask for the user to input and print menu
def menu():
    print(MENU)
    user_input = input(">>>")
    return user_input


# Show all movies from list of movies.csv file
def all_movies():
    for i in range(len(movies)):
        if movies[i][3] == "u":
            print("{}. *  {:<35} - {:>4} ({}).".format(i, movies[i][0], movies[i][1], movies[i][2]))
        else:
            print("{}.    {:<35} - {:>4} ({}).".format(i, movies[i][0], movies[i][1], movies[i][2]))


# Add new movies to list of movies.csv file
# Check user input for blank and invalid input
def add_movies():
    new_name = input("Title :")
    while not new_name:  # Check user input for blank
        print("Input can not be blank")
        new_name = input("Title :")
    # Check user input for blank, valid number and input 0
    valid = False
    while not valid:
        try:
            new_year = int(input("Year: "))
            while new_year <= 0:
                print("Number must be more than 0.")
                new_year = int(input("Year: "))
                valid = True
            valid = True
        except ValueError:
            print("Invalid input, please enter a valid number.")

    new_category = input("Category :")
    while not new_category:  # Check user input for blank
        print("Input can not be blank")
        new_category = input("Category :")
    # store user input of new data as nested list
    new_movies_lists = [new_name, new_year, new_category, "u"]
    movies.append(new_movies_lists)
    movies.sort(key=itemgetter(1, 0))
    print("{:s} ({:s} from {:d}) added to movie ".format(new_name, new_category, new_year))
    print("")


# select user watched movies to list of movies.csv file
# exception handling for user input
def watch_list():
    pass


if __name__ == '__main__':
    main()
