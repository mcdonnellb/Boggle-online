
import constants
import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('boggle_online')

high_score = SHEET.worksheet('highscore')
high_score_data = high_score.get_all_values()



class BoggleBoard:
    """
    Main Boggle Board class.
    This sets the board size,
    the number of letters to the displayed.
    This boards displays the contdown and
    has method to capture the users word
    input and validate against dictionary
    to award points for valid word entry only
    """


def __init__(self, size, num_letters, score, word_count):
    self.size = size
    self.num_letters = num_letters
    self.score = score
    self.word_count = word_count
    self.high_score = []
    self.timer = 90
    print(self)


def generate_board():
    """
    This will generate the 
    new random characters on the 
    board.
    """


board_selection =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'qu')
banner_screen()
user_name = input(' username/n')
for x in range(16):
    gen_random_sixteen = random.choices(board_selection)
    print(gen_random_sixteen)

words_entered = input("Enter your words here/n")
print(words_entered)


def points_calculation(word):
    if len(word) == 3:
        return 1
    if len(word) == 5:
        return 2
    if len(word) == 6:
        return 3
    if len(word) == 7:
        return 11
    if len(word) >= 8:
        return 11
    return 0


def new_game():
    """
    This will start a new game.
    This sets the board size,
    resets the timer and the score
    and refreshes the letters on the board.
    """


SIZE = 5

NUM_LETTERS = 16
score = 0


print("Can you find words on our online Boggle board?")
print("If you get a high score you will be added to our Boggle Hall of fame")
print("Until someone beats your score that is!!")
print(f" Board Size: {SIZE}. Number of Letters: {NUM_LETTERS}")
player_name = input("Please choose your username: \n")
print("{player_name {words entered}")
generate_board()
#new_game()
# print(high_score_data)

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

def banner_screen():

    """
    This function is to 
    ensure consistency 
    thrughout the game
    with the boggle online 
    visible throughout workflow
    """

    print(constants.WELCOME1)
    print(constants.WELCOME2)


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
print("If you get a high score you will be added to our Boggle Hall of fame")
print("Until someone beats your score that is!!")
show_menu()
new_game()
# code taken from www.codegrepper.com noted in readme
# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses


def error_in_selection():
    """
    This is to simplify code for selection error.
    user should only be able to select H, S or E
    for Menu to function
    """
    print(constants.INPUT_ERROR)
    print(constants.INPUT_ERROR2)
    print(constants.INPUT_ERROR3)
    print(constants.WELCOME1)
    print(constants.WELCOME2)
    print("++++ || You hit the wrong key        || ++++")
    show_menu()
   # elif keyboard.is_pressed('s'):
   # print(constants.SCOREBOARD)
   # break  # finishing the loop
   # print(high_score_data)
     # elif keyboard.is_pressed('h'):
     #    print(constants.INSTRUCTIONS)
    #   print("++++ || Boggle will generate 16 char grid || ++++")
    #  print("++++ || Your goal is to form words        || ++++")
    # print("++++ || They must be atleast 3 chars long || ++++")
    # print("++++ || You have 90 seconds on the clock  || ++++")
    # print("++++ || QU will count as two letters      || ++++")
    # print("++++ || A 3-letter word earns you 1 point || ++++")
    # print("++++ || A 5-letter word earns you 2 points|| ++++")
    # print("++++ || A 6-letter word earns you 3 points|| ++++")
    # print("++++ || A 7-letter word earns you 5 points|| ++++")
    # print("++++ || 8+ letters earns you 11 points    || ++++")
        
        # break



        
        # print(constants.WELCOME1)
        # print(constants.WELCOME2)
    #welcome_screen()

