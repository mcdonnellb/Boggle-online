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


print(constants.WELCOME)
print("Can you find words on our online Boggle board?")
print("If you get a high score you will be added to our Boggle Hall of fame")
print("Until someone beats your score that is!!")
print("++++ ||For Help please hit the H Key      || ++++")
print("++++ ||For Scoreboard please hit the S Key|| ++++")
print("++++ ||To start a game hit Enter Key      || ++++")

player_selection = input("Please select Option H, S or Enter: \n")

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
