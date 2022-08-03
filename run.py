# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

scores = {"computer": 0, "player": 0}
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

def new_game():
            """
            This will start a new game.
            This sets the board size,
            resets the timer and the score
            and refreshes the letters on the board.
            """
            size = 5
            scores["player"] = 0
            print("Welcome to Boggle Online")
            print(f" Board Size: {size}. Number of Letters: {num_letters}")
            player_name = input("Please choose your username: \n")
new_game()
