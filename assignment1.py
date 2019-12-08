"""
Replace the contents of this module docstring with your own details
Name: Kyaw Soe Naing
Date started: 29/11/2019
GitHub URL: https://github.com/Ezra2952/assignment-01-Ezra2952
"""

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
lines = Database.readlines()
# all data from csv file is stored in movies = [] as nested list
movies = []
Database.close()
print("{:d} movies loaded".format(len(lines)))


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


# ask for the user to input and print menu
def menu():
    print(MENU)
    user_input = input(">>>")
    return user_input


# Show all movies from list of movies.csv file
def all_movies():
    pass


# Add new movies to list of movies.csv file
def add_movies():
    pass


# select user watched movies to list of movies.csv file
# exception handling for user input
def watch_list():
    pass


if __name__ == '__main__':
    main()
