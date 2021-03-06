Pitchd
# Description
A flask-based application that allows users to post elevator pitches, get and give feedback on the pitches.

By https://github.com/Kennedy128/ken-project2
# Setup/Installation Requirements
* $Prerequisites
* $python3.8
* $pip
* $Virtual environment(virtualenv)
* $Flask-Mail
* $PostgreSQL
# Cloning and running
* Clone the application using git clone(this copies the app onto your device). In your terminal:
* $ git clone https://github.com/Kennedy128/ken-project2

* $ cd pitch

## Use the following commands in your terminal to create virtual environment
$ python3.6 -m venv --without-pip virtual

$ source virtual/bin/env

$ curl https://bootstrap.pypa.io/get-pip.py | python

Installing Flask and other Modules
$ python3.6 -m pip install Flask

$ python3.6 -m pip install Flask-Bootstrap

$ python3.6 -m pip install Flask-Script

$ python3.6 -m pip install Flask-Mail

# KNOWN BUGS
none so far

# Testing the Application
To run the tests for the class files:
$ python3.6 manage.py test

# Technologies Used
* Python 3.6
* Flask
# BDD
Behavior	Input Example	Output
* User Sort Preference	Category	Sorted Pitches by Categories
* Send user to email to confirm sign up	Click 'sign up'	Send email
* Show pitches from other users	select a specific category	List pitches
* Enable user to give reviews and feedback for a pitch	Click 'new review'	written user review
* Enable vote for a pitch	Click 'like' or 'dislike'	user vote
* Enable user write a pitch	Click 'new pitch'	written user pitch
* Live Site *Can be accessed here https://pitch-kenne.herokuapp.com/

# Author's Contact
If you need any clarifications or have feedback on this project , contact the author at kennedymbithi12@gmail.com

# License
This software is Licensed under MIT license Copyright (2018) https://raw.githubusercontent.com/Kennedy128/ken-project2/master/LICENSE