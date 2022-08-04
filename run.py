
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


SIZE = 5

NUM_LETTERS = 16
# scores["player"] = 0
print(f" Board Size: {SIZE}. Number of Letters: {NUM_LETTERS}")
player_name = input("Please choose your username: \n")
new_game()
# print(high_score_data)


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
print("++++ || For Help please hit the H Key      || ++++")
print("++++ || For Scoreboard please hit the S Key|| ++++")
print("++++ || To start a game hit Enter Key      || ++++")

player_selection = input("Please select Option H, S or Enter: \n")

new_game()
# code taken from www.codegrepper.com noted in readme
#https://stackoverflow.com/questions/24072790/how-to-detect-key-presses

#user_input = input()
#options = ("H", "S", "E")
#if user_input == "E":
 #   print("You Pressed Enter !/n")
  #  welcome_screen()
#if user_input not in options:
 #   print("uh oh")
  #  error_in_selection()


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
    print("++++ || Choose Enter to start a game || ++++")
    print("++++ || Choose S to view Scoreboard  || ++++")
    print("++++ || Choose H for Help            || ++++")
    player_selection = input("Please select Option H, S or Enter: \n")
   # elif keyboard.is_pressed('s'):
    #        print(constants.SCOREBOARD)
     #       # break  # finishing the loop
      #      print(high_score_data)
       # elif keyboard.is_pressed('h'):
        #    print(constants.INSTRUCTIONS)
         #   print("++++ || Boggle will generate 16 char grid || ++++")
          #  print("++++ || Your goal is to form words        || ++++")
           # print("++++ || They must be atleast 3 chars long || ++++")
            # print("++++ || You have 90 seconds on the clock  || ++++")
            # print("++++ || QU will count as two letters      || ++++")
            #print("++++ || A 3-letter word earns you 1 point || ++++")
            #print("++++ || A 5-letter word earns you 2 points|| ++++")
            #print("++++ || A 6-letter word earns you 3 points|| ++++")
            #print("++++ || A 7-letter word earns you 5 points|| ++++")
            #print("++++ || 8+ letters earns you 11 points    || ++++")
        
        #break



        
        # print(constants.WELCOME1)
        #print(constants.WELCOME2)
    

    #welcome_screen()


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
