import random
import gspread
from google.oauth2.service_account import Credentials
import constants
import re
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('boggle_online')

high_score = SHEET.worksheet('scores')
high_score_data = high_score.get_all_values()


def get_random_choice():
    return random.choices(board_selection)


def generate_board():
    board_selection = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'QU')
    grid = []
    guesses = []
    score = 0 
    
    for i in range(8):
        grid.append(random.choices(board_selection, k=8))
        print(grid[i])
    words_entered = input("Enter your words here with a space in between each: ")
    if not re.match("^[a-z , ]*$", words_entered):
        print ("Error! Only  a-z selection allowed!")
        words_entered = input("Try again - Enter your words here: ")
    if not re.match("^[a-z , ]*$", words_entered):
        print ("Please go back and read the instructions")
    guess_list = words_entered.split(",")
    guesses.append(words_entered)
    print("Here are the words you found", guess_list)
    print(len(words_entered))
    return guess_list 
# code taken from www.codegrepper.com noted in readme
# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses


def end_game():
   
    """
    This function is to 
    end the game, show the end game 
    graphics and call the crucial
    functions which determine
    if words entered are valid
    and if so the score
    This will also determine if 
     user has high score
    which will then be pushed 
    to the google sheet
    """
    
    print(constants.TIME_IS_UP1)
    print(constants.TIME_IS_UP2)
    print(constants.TIME_IS_UP3)
    print("Calculating your points....")
    print("Checking to see if you have reached a high score")
    print("Are you brave enough to try again")
    welcome_screen()


            
def main_menu():
    user_selection = input("Enter 'YES' to start a game. "
    "Enter S for High Scores, H for Help Menu or any other UPPER letter to exit the game: "
    )
    if not re.match("^[A-Z]*$", user_selection):
       print ("Error! Only  a-z selection allowed!")
       user_selection = input(" TRY AGAIN -Enter 'YES' to start a game. "
             "Enter S for High Scores, H for Help Menu or any other UPPER letter to exit the game: "
             )
    if user_selection .upper() == 'YES' or user_selection .upper() == 'Y':
       user_name = input(" Enter username:")
       print("Let's go " + user_name + '!')   
       generate_board()
       end_game()
    elif user_selection .upper() == 'H':
         print("++++ || Welcome to the Help page                                                                             || ++++")
         print("++++ || The aim of the game is simple                                                                        || ++++")
         print("++++ || To find as many words as you can in the grid                                                         || ++++")
         print("++++ || Can you find words upside down, diagnolly, hoirzontally? Let's kick that brain into action!          || ++++") 
    elif user_selection .upper() == 'S':
        print(constants.SCOREBOARD)
        print("++++ || Welcome to the High Score page                                                                  || ++++")
        print("++++ || The Boggle Hall of fame                                                                         || ++++")
        print("++++ || Do you have what it takes to beat our superstars?                                               || ++++")
        high_score = SHEET.worksheet('scores')
        high_score_data = high_score.get_all_values()
        print(high_score_data)     
    else:
        print("Thank you")  
        print("You have opted to exit") 
        sys.exit()


def welcome_screen():
    """
    This is the landing screen
    when the program is first
    run and will be the main
    page for nav purposes
    """
    print(constants.WELCOME1)
    print(constants.WELCOME2)
    print("Can you find words on our online Boggle board?")
    print("Get a high score to be added to the hall of fame")
    print("++++ || Welcome to Boggle online                 || ++++")
    print("++++ || Created by Bee in 2022                   || ++++")
    print("++++ || To reimagine the 90's classic            || ++++")
    main_menu()
welcome_screen()
    
