import random
import gspread
from google.oauth2.service_account import Credentials
import constants

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
print(high_score_data)

def get_random_choice():
    return random.choices(board_selection)
# function to calculate the points achieved in the course of the game
def points_calculation(words_entered):
    if len(words_entered) == 3:
        return 1
        print("your score is 1")
    if len(words_entered) == 5:
        return 2
        print("your score is 2")
    if len(words_entered) == 6:
        return 3
    if len(words_entered) == 7:
        return 11
    if len(words_entered) >= 8:
        return 11
    return 0



def generate_board():
    board_selection = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'QU')
    grid = []
    guesses = []
    
    for i in range(8):
        grid.append(random.choices(board_selection, k=8))
        print(grid[i])
    words_entered = input("Enter your words here: ")
    guess_list = words_entered.split(",")
    print("Here are the words you found", guess_list)
    return guess_list 


# code taken from www.codegrepper.com noted in readme
# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses


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
    print("++++ || For Help please hit the H Key      || ++++")
    print("++++ || For Scoreboard please hit the S Key|| ++++")
    print("++++ || To start a game hit Enter Key      || ++++")
    player_selection = input("Please select Option H, S or Enter: \n")
    user_name = input(" Enter username:")
    print("Let's go " + user_name + '!')
    generate_board()
welcome_screen()



def end_game():
   
    # """
    # This function is to 
    # end the game, show the end game 
    # graphics and call the crucial
    # functions which determine
    # if words entered are valid
    # and if so the score
    # This will also determine if 
    # user has high score
    # which will then be pushed 
    # to the google sheet
    #"""
    if attempts >= 10:
        print(constants.TIME_IS_UP1)
        print(constants.TIME_IS_UP2)
        print(constants.TIME_IS_UP3)
        #points_calculation()
        print("Calculating your points....")
        #check_if_high_score()
        print("Checking to see if you have reached a high score")
        #points_calculation(()))
        #print(score)



def update_worksheet(data, worksheet):
     """
    This function checks the score on the spreadsheet and if current score is higher updates the values 
    """
while True:
        current_score = SHEET.worksheet("scores").get_all_values()
        print(f"Updating {SHEET} worksheet...\n")
        worksheet_to_update = SHEET.worksheet("scores")
        worksheet_to_update.append_row(data)
        update_worksheet(high_score_data, "scores")
        print(f"{worksheet} ScoreBoard updated successfully\n")
        print(high_score_data)

def show_menu():

    """
    This function is to
    ensure consistency
    thrughout the game
    with the menu items
    visible throughout workflow
    in critical screens to ensure
    positive UX experience
    """
    print(constants.WELCOME1)
    print(constants.WELCOME2)
    print("++++ || For Help please hit the H Key      || ++++")
    print("++++ || For Scoreboard please hit the S Key|| ++++")
    print("++++ || To start a game hit Enter Key      || ++++")
    player_selection = input("Please select Option H, S or Enter: \n")


def error_in_selection():
    """
    This is to simplify code for selection error.
    user should only be able to select H, S or E
    for Menu to function
    """
    print(constants.INPUT_ERROR)
    print(constants.INPUT_ERROR2)
    print(constants.INPUT_ERROR3)
    print("++++ || You hit the wrong key        || ++++")
    