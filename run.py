import keyboard
import constants
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('boggle_online')

sales = SHEET.worksheet('sales')
high_score = SHEET.worksheet('highscore')
high_score_data = high_score.get_all_values()

data = sales.get_all_values()

print(data)


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


def welcome_screen():
    """
    This will start a new game.
    This sets the board size,
    resets the timer and the score
    and refreshes the letters on the board.
    """


print(constants.WELCOME1)
print(constants.WELCOME2)
print("Can you find words on our online Boggle board?")
print("If you get a high score you will be added to our Boggle Hall of fame")
print("Until someone beats your score that is!!")
print("++++ || For Help please hit the H Key      || ++++")
print("++++ || For Scoreboard please hit the S Key|| ++++")
print("++++ || To start a game hit Enter Key      || ++++")

player_selection = input("Please select Option H, S or Enter: \n")
# code taken from www.codegrepper.com nored in readme
while True:  # making a loop
    try:  
        if keyboard.is_pressed('enter'):  # if key 'q' is pressed
            print('You Pressed Enter !')
        elif keyboard.is_pressed('s'):
            print(constants.SCOREBOARD)
            # break  # finishing the loop
            print(high_score_data)
        elif keyboard.is_pressed('h'):
            print(constants.INSTRUCTIONS)
            print("Boggle will generate a board with 16 characters")
            print("You must construct from characters in a row")
            print("They must be atleast 3 chars long")
            print("You will have 90 seconds to capture as many as possible")
    except:
        
        break 
    
        print(constants.WELCOME1)
        print(constants.WELCOME2)
        print("++++ || You hit the wrong key        || ++++")
        print("++++ || Choose Enter to start a game || ++++")
        print("++++ || Choose S to view Scoreboard  || ++++")
        print("++++ || Choose H for Help            ||  ++++")

    welcome_screen()


def new_game():
    """
    This will start a new game.
    This sets the board size,
    resets the timer and the score
    and refreshes the letters on the board.
    """


SIZE = 5

NUM_LETTERS = 16
# scores["player"] = 0
# print(f" Board Size: {SIZE}. Number of Letters: {NUM_LETTERS}")
# player_name = input("Please choose your username: \n")
# new_game()
# print(high_score_data)
