![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

+ [User Experience](#userexperience "User Experience")
  + [User Stories](#user-stories "User Stories")
  + [User Goals](#user-goals "User Goals")
  + [Requirements](#requirements "Requirements")
  + [Design](#design "Design")
    + [Typography](#typography "Typography")
    + [Common Features](#commonfeatures "Common Features")
+ [Accessibility](#accessability "Accessability")
  + [Testing](#testing "Testing")
    + [Functionality](#functionality "Functionality")
    + [Styling](#styling "Styling")
    + [Error Log](#errorlog "Error Log")
    + [Python Validation](#pythonvalidation "Python Validation")
    + [HTML Validation](#htmlvalidation "HTML Validation")

  + [Citations](#citations "Citations")
+ [Lessons Learned](#lessons-learned “Lessons Learned")
+ [Quirks](#quirks "Quirks")
  + [Future Features](#future-features "Future Features")

  ## Boggle Online - Assignment Purpose 

I chose to reimagine the 90's game 'Boggle' which was a physical game with an 8x8 grid, before the timer starts one user would shake the boggle board, remove the lid and start the timer. It would then be on the players to doucment as many words as possible using the letters on the board that are either in a row, or diagnally in a row.

The rules for playing Boggle are as follows:
* Each word should be of at least three letters.
* Words that have the exact spelling but different meanings will be counted only once.
* You cannot repeat any words.
* You can use both singular and plural forms of the same word.
* The QU cube counts as two letters.

The user with the most words then wins.

I chose this game both  to keep up with my theme of 90's nostalgia, but also because I felt this would be an approoprirate game for deployment within this command line environment. 



## User Experience 

Critical Objectives:

## User Stories

## User Goals 

* End user Goal
The application user wants to play a logic game

* Site owner's goal:

The Boggle game will generate a board of 4 x 4 characters, the objective of the game is to find as many words as possible before the time is up. 
The application provides a working boggle game for a single user to play against the computer



## Requirements
Project Purpose:

In this project, Portfolio 3,  the requirment was to build a command-line application that allows your users to manage a common dataset about a particular domain.
As part of Project 3 - python Computer Program Development, the following are required 
* Python

* Heroku app 

* Google API (required to attain more than pass grade)


#### Overall requirements of Assessment:

*  Implement a given algorithm as a computer program
*  Adapt and combine algorithms to solve a given problem
*  Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)
*  Explain what a given program does
*  Identify and repair coding errors in a program
*  Use library software for building a graphical user interface, or command-line interface, or web application, or mathematical software
*  Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
*  Demonstrate and document the development process through a version control system such as GitHub
*  Deploy a command-line application

## UX Design 

#### User Control

#### Consistency

#### Confirmation

#### Development and Implementation
* Readability
    How I kept my code as clean as possible and used started descriptive naming conventions
* Defensive Design
    all input data is validated (e.g. presence check, format check, range check)
    internal errors are handled gracefully, and users are notified of the problem where appropriate.
* Comments

* Compliant Code
* Robust code


* Version Control Software - Git

For this project I was very conscious that I used the version control software is effectively, per Code Institite / best practices:

* all code  managed in git with commit messages that reflect the specific reason for the commit
with is a separate, defined commit for each feature/fix
there are no  large commits which make it harder to understand the development process and could lead the assessor to suspect plagiarism


## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly




## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

## Deployment Details

The project was deployed using the Code Institute terminal for Heroku. In order to deploy I completed the following:

* I cloned the Python / projext 3 repository
* I created a new Heroku app
* I set the buildbacks from the settings tab to Python and NodeJS
* I linked tjhe Heroku app to my repository
* I clicked on the deploy optiohn 

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

## Google API





#### Python Validation

## Testing 
I have manually tested my project by completing the folling steps:
* Run the code through the PEP8 linter and confirmed all errors were cleared.
* Tested mulitple inputs to ensure only valid data is accepted, and errors thrown in appropritate situations
* Tested in both my local terminal and the Code Institute Heroku Terminal to ensure testing is thorough.

## Error Log 
The below  are issues I encountered over the course of this Python program development:

*
*
*
*
*
*

## Solved Issues 
## Remaining Bugs 

## future Development
This game is best suited as a multi-player game which would really enhance the user experience and emotional attachement to the game. This is something I plan on working on for future iterations.


## Validation Testing
* PEP8 - as per below picture there were no errros retured from https://PEP8online.com  

## Citations
First and foremost a huge thank you to Martina my mentor who has been extremely helpful in all of my assignemnets, but in particular with the Python assignment.

Kasia Bogucka, the course cohort leader who has been filling the cohort with confidence even on our bad days when we are struggling with our code, we end up leaaving our meeetings with a smile and a renewed positivity that we can achieve our goals.

The tutor support was something I have become more comfortbale using, and the team are really fantastic at their job. It is not a case of giving you the answer buy making you think ciritcally about the issue you are facing, and core concepts that you covered over the course of the online content.

#### TOC
Taken from my last assignment with hints taken from the below website:

#### Media 


#### 