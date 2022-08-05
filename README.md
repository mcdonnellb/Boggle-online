![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

![Terminal window](/workspace/Boggle-online/documentation/images/terminal_window_screenshot1.jpg)




+ [Assignment Purpose](#assignmentpurpose "Assignment Purpose")
+ [User Experience](#userexperience "User Experience")
+ [User Stories](#user-stories "User Stories")
+ [User Goals](#user-goals "User Goals")
+ [Requirements](#requirements "Requirements")
+ [Game Workflow](#gameworkflow "Game Workflow")
+ [Design](#design "Design")
+ [Accessibility](#accessability "Accessability")
+ [Deployment Details](#deployment-details "Accessability")
+ [Testing](#testing "Testing")
    + [Functionality](#functionality "Functionality")
    + [Error Log](#errorlog "Error Log")
    + [Python Validation](#pythonvalidation "Python Validation")
    + [HTML Validation](#htmlvalidation "HTML Validation")
+ [Citations](#citations "Citations")
+ [Quirks](#quirks "Quirks")
+ [Future Features](#future-features "Future Features")

## Boggle Online 
#### Assignment Purpose 

I chose to reimagine the 90's game 'Boggle' which was a physical game with an 8x8 grid, before the timer starts one user would shake the boggle board, remove the lid and start the timer. It would then be on the players to doucment as many words as possible using the letters on the board that are either in a row, or diagnally in a row.

The rules for playing the original Boggle are as follows:
* Each word should be of at least three letters.
* Words that have the exact spelling but different meanings will be counted only once.
* You cannot repeat any words.
* You can use both singular and plural forms of the same word.
* The QU cube counts as two letters.

The user with the most words then wins.

I chose this game both  to keep up with my theme of 90's nostalgia, but also because I felt this would be an approoprirate game for deployment within this command line environment. 

Boggle online will be true to it's 90's self with the same simplistic rules, the biggest difference will be that the computer will be in lieu of a real opponent, using the google API to check validity of the words entered, and push to the high score sheet if user has attained a score higher than those already on the list.

The live version of my project is available at the below link:

https://boggle-online.herokuapp.com/

#### User Experience 

Critical Objectives:

#### User Stories

#### User Goals 

* End user Goal
- The application user wants to play a logic game based upon a classic board game
- The application user wants to be challenged and entertained
- The application user wants to know at all times what is happening, how to navigate, options etc


* Site owner's goal: 
- The site owner goal is to provide a functioning, challenging game for a single user to play against the computer
- The goal is to create an application as close to the original 90's Boggle game as is achievable within a command line application.
- The goal is to create a workflow that is straightforward and thoughful
- The goal is to create a program that end users will want to return to.


#### Overall requirements of Assessment:
Project Purpose:

In this project, Portfolio 3,  the requirment was to build a command-line application that allows your users to manage a common dataset about a particular domain.
As part of Project 3 - python Computer Program Development, the following items were required:

*  Implement a given algorithm as a computer program
*  Adapt and combine algorithms to solve a given problem
*  Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)
*  Explain what a given program does
*  Identify and repair coding errors in a program
*  Use library software for building a graphical user interface, or command-line interface, or web application, or mathematical software
*  Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
*  Demonstrate and document the development process through a version control system such as GitHub
*  Deploy a command-line application


## Game Workflow
- The user is presented with  a simple name input field
- The user is then asked if they want Help H, New Game N, High Score H
- If the user hits H the game instructions populate the screen, with the options for High Score and New Game remaining.
- If the user hits N the New Game Screen Displays - user must input their username which must contain 9 or less alphanumeric characters, special characters are not accepted.
- When the User hits S for Start the board is presented to the screen with 4 x 4 grid containing letters
- At this point the timer starts counting down from 1min 30 seconds
- The user has this time to enter as many words as possible, they must contain at least 3 letters
- The program will run the words entered by the user to confirm they are genuine words
- The program will return the users score along with the username
- The program will add this score and name to the High Score Array, if it is indeed a high score.
- The user will be presented with the end game screen. 

![Game Workflow](/workspace/Boggle-online/documentation/images/python_workflow_thought_process.jpg)

## Design 
I opted for bold ASCII art to try and enhance the appearance of my application. My initial iteration did not have this art and from feedback, users advised they would feel more inclined to return to the current application due to the osiitive emotional response they had when playing.

#### User Control
* simplfied menu options to ensure user has ease of navigation through program


#### Confirmation

I added the following options to allow a user know that their data is good:
* Print confirmation Messages following on from data input 
* I added a simple banner menu to reiterate the options to users and simplify UI / reduce risk of losing track of screen options

I added the following to let the user know they had entered bad data: 
* Print Message outlining what the issue is and what is expected 
* 

#### Development and Implementation

## Deployment Details

The project was deployed using the Code Institute terminal for Heroku. In order to deploy I completed the following:

* I cloned the Python / project 3 repository and renamed / saved into my own GitHub repository.
* I enabled Google Sheets API and Google Drive API
* I created a service account and generated a creds.json file and added this to Gitpod
* I added a line to gitignore so that the creds file would not be added to pushed with the commits for security reasons.
* I created a new Heroku app with region set to Europe
* I set the buildbacks from the settings tab to Python and NodeJS
* I created a config var for creds so that Heroku can access google APIs.
* I created a config var called `PORT` and set this value to `8000`
* I linked the Heroku app to my GITHUB repository
* I clicked on the deploy option 


#### Google API
I took inspiration from the Love Sandwiches project and decided to use a similar apporach to my computer Program, using Google Sheets to store data/ add data/ query data.


#### Testing

I have manually tested my project by completing the folling steps:

* Run the code through the PEP8 linter and confirmed all errors were cleared.
* Tested mulitple inputs to ensure only valid data is accepted, and errors thrown in appropritate situations
* Tested in both my local terminal and the Code Institute Heroku Terminal to ensure testing is thorough.


![PEP8 validation](/workspace/Boggle-online/documentation/images/python_workflow_thought_process.jpg)

## Error Log 
The below  are issues I encountered over the course of this Python computer program development:

* Authentication issue with Google Sheets API- I had accidentally configured an API Key which was why I could not access my Google Sheets spreadsheet and kept getting the below error. As it transpired I also had a space in the file name which was not visible to the naked eye until you copy it and note the space, once the space was remove data was loaded without issue. 
    gspread.exceptions.SpreadsheetNotFound
* In order for input methods to work  correctly in the deployed mock terminal,  
I added a new line character at the  end of the text inside the input method.  
Without this extra line, the text for the import  request will not show up in the terminal.   
* I got the initial gspread error when the code was deployed to Heroku which needed to be addressed with some additions to my requirements.txt file.
* Timer was running independently so I needed to go back and check through my code, and I realised the function needed to be called after the characters were generated
* Boggle Board Grid was either displaying 16 random characters in one line, or a grid of 4x4 with the top line containing random characters, and the lines below repeating the same characters.
* 



## Remaining Bugs 
* Timer was not working so was removed - please ignore any references 

* validation checks  was not working so was removed
*  score check and dictionary check were not working so removed.


## Quirks
* One quite obvious quirk is my Boggle Board having square brackets and commas still intact. This was something I hoped to remove but I actually think the square brackets help give the board a grid- like appearance.

* The timer is hidden as I was unable to prevent this from overwriting the user input text. It still runs in the background, you just can't see it or see how much time is left which is a shame.


## Future Development
* This game is best suited as a multi-player game which would really enhance the user experience and emotional attachement to the game. This is something I plan on working on for future iterations.
* I would definitley improve upon the game logic, only allowing a certain number of vowels, consonats and 1/2 Qu characters.
* I would also add logic for the computer to calculate the amount of English words found on the board and then run a comparison to what the end user found.

## Validation Testing
* PEP8 - as per below picture there were no errros retured from https://PEP8online.com  

## Citations
First and foremost a huge thank you to Martina my mentor who has been extremely helpful in all of my assignemnets, but in particular with the Python assignment.

Kasia Bogucka, the course cohort leader who has been filling the cohort with confidence even on our bad days when we are struggling with our code, we end up leaaving our meeetings with a smile and a renewed positivity that we can achieve our goals.

The tutor support was something I have become more comfortbale using, and the team are really fantastic at their job. It is not a case of giving you the answer. By making you think ciritcally about the issue you are facing, you are steered back to core concepts that you covered over the course of the online content. Massive thank you to all at Code Institute for thier patience and can do attitude, inspiring us all to keep going.

#### TOC
Taken from my last assignment with hints taken from the below website:


#### Media 
Flow chart created through Mural:
https://app.mural.co/

## Inspiritation
I relied heavily on the experience gained from the Love Sandwiches Project and used this as my basis for creating my application. I also sought inspiration from the battleships example given by Code Institute in terms of the logic used to create the application.

#### Websites:
* I used the below website to generate fun grpahics to enhance the aesthetics of the game and improve UX usability 
    https://fsymbols.com/generators/carty/   
* I used the following Cheat Sheet to help me with my readme file:
    https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* I sought some inspiration from the following links to help me decide on the best approach for my program:
    https://www.freecodecamp.org/news/how-to-build-a-wordle-clone-using-python-and-rich/
    https://www.freecodecamp.org/news/how-to-build-a-wordle-clone-using-python-and-rich/


#### Code Sources 
* I used the below code to help me create code for my button pressed functionality
    https://www.codegrepper.com/code-examples/python/python+detect+button+press 

* I used the below site and code for my timer functionality with minor tweaks based on my own requirements for the app:
    https://www.programiz.com/python-programming/examples/countdown-timer

* I used a dictionary file taken from the below GITHUB, This is to confirm the words chosen are in fact dictionary verified words.
    https://github.com/dwyl/english-words

#### Modules
I installed the following Modules for my project
* GSPREAD -allow use of Google sheets api
* Keyboard capture keyboard input
* Random    to allow ease of creating boogle board random characters
