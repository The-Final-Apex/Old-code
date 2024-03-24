"""
This Module Was Created By Apex862
A.K.A  Ethan

Abo is a multi function Desktop tool capable of opening apps, taking photos creating both py and txt files

installing modules and apps on Two Linux Distributions e.t.c., and it is completely OPEN SOURCE

Feel free to add anything on GitHub https://github.com/Apex862-2/Abo/tree/main

See the Documentation for more info  https://github.com/Apex862-2/Abo/blob/main/README.md
"""

from ecapture import ecapture as ec
from ecapture import *
import os
import smtplib
import webbrowser
from datetime import datetime
import Abo_piano
import Abo_Errors
import random


def _help():
    """Help links and MD"""
    print("See documentation for more info  https://github.com/Apex862-2/Abo/blob/main/README.md ")
    print("see Abo.md for info incase of offlin-  , offlin-i , offlininess i guess?")


def installU(req):
    """this function works only for ubuntu to install apps alone via terminal"""
    try:
        os.system(f'sudo apt get install {req}')
    except NameError:
        print("wrong name given")
    except ConnectionError:
        print("please connect to the internet")
    except RuntimeError:
        print("Error this is not a problem with names or internet")


def installF(reqq):
    """This function applies only to installing apps on fedora via terminal"""
    try:
        os.system(f'sudo dnf install {reqq}')
    except NameError:
        print("wrong name given")
    except ConnectionError:
        print("please connect to the internet")
    except RuntimeError:
        print("Error this is not a problem with names or internet")


def install(module):
    """Installs a python modile"""
    try:
        os.system(f'pip install {module}')
    except RuntimeError:
        exec(f'python3 pip install {module}')
    except ConnectionError:
        print("Bruh, you ain't connected to the internet AHHHHHHHHHH!")


def openp(app):
    """opens the app specified  using os  str accepted also var -PLEASE- BE !!CAREFULLLLLLLLLLL!! IT'S A BIT WONKY"""
    app = app.lower()
    print("Opening..")
    print(app)
    print("..")
    print("..")
    os.system(app)


def getchords(mood):
    """gets piano or guitar chords from Abo_piano.py vars and strings"""
    Abo_piano.chords(mood)


def webopen(search, engine):
    """searches google for your query  google is default
    supports Bing, Google, and DuckDuckGo
    """
    try:
        if engine == "google" or "Google" or "GOOGLE":
            webbrowser.open(f'https://www.google.com/search?client=firefox-b-d&q={search}')
        elif engine == "duckduckgo" or "DuckDuckGo" or "DUCKDUCKGO" or "Duck-Duck-Go" or "Duck" or "duck":
            webbrowser.open(f'https://duckduckgo.com/?t=ffab&q={search}')
        elif engine == "bing" or "BING" or "Bing":
            webbrowser.open(f'https://www.bing.com/search?q={search}&search=&form=QBLH')
        else:
            webbrowser.open(f'https://www.google.com/search?client=firefox-b-d&q={search}')
    except ConnectionError:
        print(f'Error:{random.choice(Abo_Errors.weberrors)}')


def sendEmail(to, content, id, psswd):
    """sends an Email  Untested because I don't have many test subje... I mean friends to email"""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        # Enable low security in gmail
        server.login(id, psswd)
        server.sendmail(id, to, content)
        server.close()
    except ConnectionError:
        print(f'Error:{random.choice(Abo_Errors.weberrors)}')


def Time():
    """tells the time"""
    strtime = datetime.now().strftime("%H:%M:%S")
    print(f"the time is {strtime}")


def music(dire):
    """plays music untested because I have bad audio drivers and I don't want to log in or download sound stuff"""
    try:
        print("Make Sure You Gave Me A Valid Music Path To Go To! Not The Song File")
        print("The File Must Contain Only Music:")
        songs = os.listdir(dire)
        print("songs: ", songs)
    except FileNotFoundError:
        print(f'Error:{random.choice(Abo_Errors.notafile)}')


def takepic():
    """takes a picture  failed  cant turn camera off do not use"""
    cam = ec
    print("wait a moment...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print(f"Errror:{random.choice(Abo_Errors.camerrors)}")
    # cam.capture(0, "Camera ", "img.jpg")


def createfile(name, content):
    """creates a txt file"""
    note = content
    strtime = datetime.now().strftime("%H:%M:%S")
    file = open(f'{name}.txt', 'w')
    strtime = datetime.now().strftime("%H:%M:%S")
    file.write(strtime)
    file.write(" :- ")
    file.write(note)


def create_python(script_name, complexity_level):
    """creates a python file"""
    global script_func
    if complexity_level == "complex":
        script_func = """
    def main():
        print("Hello From Abo")
        pass

    if __name__ == "__main__":
        main()
    """
    elif complexity_level == "game":
        script_func = """
import sys
import pygame

pygame.init()

# create a display surface
display_width = 800
display_height = 600
display_surface = pygame.display.set_mode((display_width, display_height))

# set the title of the game
pygame.display.set_caption('My 3D Game Engine')

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update game objects
    # render game objects
    pygame.display.update()

    """
    elif complexity_level == "simple":
        script_func = """
    print("Hello, World!")
    """
    elif complexity_level == "3d":
        script_func = """
# Import required libraries
import pygame
from OpenGL.GL import *

# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF|pygame.OPENGL)

# Set up OpenGL
glViewport(0, 0, 800, 600)
glClearColor(0.5, 0.5, 0.5, 1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, 800/600, 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Main loop
running = True
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Render 3D objects
    # ...

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
"""
    # Create script file and write function
    with open(script_name + ".py", "w") as f:
        f.write(script_func)

    print("Script created successfully!")



    greetings = ["Hello From Abo", "Greetings This is Abo", "Salutations from Abo",
                 "HELLO FROM ABO", " Documentation: https://github.com/Apex862-2/Abo/blob/main/README.md ", "Abo!!!",
                 "Hi from Abo", "This is Abo",
                 "HI FROM THE ABO COMMUNITY"]
    print(random.choice(greetings))

# ____________________________________________________
