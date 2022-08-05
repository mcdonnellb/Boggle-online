
import constants 
import time      
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
gridl= []
grid = []

#def end_game():
   
    #"""
    #This function is to 
    #end the game, show the end game 
    #graphics and call the crucial
    #functions which determine
    #if words entered are valid
    #and if so the score
    #This will also determine if 
    #user has high score
    #which will then be pushed 
    #to the google sheet
    #"""
#print(constants.TIME_IS_UP1)
#print(constants.TIME_IS_UP2)
#print(constants.TIME_IS_UP3)
#points_calculation()
#check_if_high_score()

def show_banner_screen():

    """
    This function is to 
    ensure consistency 
    thrughout the game
    with the boggle online 
    visible throughout workflow
    """

    print(constants.WELCOME1)
    print(constants.WELCOME2)


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

#print(constants.TIME_IS_UP1)
#print(constants.TIME_IS_UP2)
#print(constants.TIME_IS_UP3)
  

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
    print(self)

board_selection = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z', 'QU')
show_banner_screen()
USER_NAME = input(' Enter username:')
print("Let's go " + USER_NAME + '!')
gen_random_sixteen = random.choices(board_selection)
for x in range(16):
    gen_random_sixteen = random.choices(board_selection)

for i in range(5):
    gen_random_sixteen = random.choices(board_selection)
    gridl.append(gen_random_sixteen)

for i in range(4):
    #gen_random_sixteen = random.choices(board_selection)
   grid.append(list(gridl))
   #grid.append(gen_random_sixteen)
   print(gridl)

words_entered = input("Enter your words here: ")
countdown(90)
#end_game()

#function to calculate the points achieved in the course of the game
def points_calculation(words_entered):
    if len(words_entered) == 3:
        return 1
    if len(words_entered) == 5:
        return 2
    if len(words_entered) == 6:
        return 3
    if len(words_entered) == 7:
        return 11
    if len(words_entered) >= 8:
        return 11
    return 0

#def check_if_high_score(score):
   # if score > 

    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} ScoreBoard updated successfully\n")

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


#def welcome_screen():
    """
    This is the landing screen
    when the program is first
    run and will be the main
    page for nav purposes
    """


#print(constants.WELCOME1)
#print(constants.WELCOME2)
#print("Can you find words on our online Boggle board?")
#print("If you get a high score you will be added to our Boggle Hall of fame")
#print("Until someone beats your score that is!!")
#show_menu()
#new_game()
# code taken from www.codegrepper.com noted in readme
# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses


def error_in_selection():
    """
    This is to simplify code for selection error.
    user should only be able to select H, S or E
    for Menu to function
    """
    show_banner_screen()
    print(constants.INPUT_ERROR)
    print(constants.INPUT_ERROR2)
    print(constants.INPUT_ERROR3)
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

