# Importing necessary packages
import tkinter as tk
from tkinter import *

import pytube
from pytube import YouTube
from tkinter import messagebox, filedialog
import cv2


# Defining CreateWidgets() function
# to create necessary tkinter widgets

def Widgets():

    head_label = Label(root, text="YouTube Video Downloader",
                    padx=15,
                    pady=15,
                    bg="#000112",
                    fg="red",
                    font = "SegoeUI 14",
                    )
    head_label.grid(row=1,
        column=1,
        pady=10,
        padx=5,
        columnspan=3)

    link_label = Label(root,
                    text="YouTube link :",
                    bg="#000000",
                    fg="#ffffff",
                    pady=5,
                    padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                        width=35,
                        textvariable=video_Link,
                        font="Arial 14")
    root.linkText.grid(row=2,
                    column=1,
                    pady=5,
                    padx=5,
                    columnspan=2)


    destination_label = Label(root,
                            text="Destination :",
                            bg="#000000",
                            fg="#ffffff",
                            pady=5,
                            padx=9)
    destination_label.grid(row=3,
                        column=0,
                        pady=5,
                        padx=5)


    root.destinationText = Entry(root,
                                width=27,
                                textvariable=download_Path,
                                font="Arial 14")
    root.destinationText.grid(row=3,
                            column=1,
                            pady=5,
                            padx=5)


    browse_B = Button(root,
                    text="Browse",
                    command=Browse,
                    width=10,
                    bg="#3d3846",
                    relief=GROOVE)
    browse_B.grid(row=3,
                column=2,
                pady=1,
                padx=1)

    Download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        bg="#3d3846",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)


# Defining Browse() to select a
# destination folder to save the video

def Add_img(image):
    #
    # # Load the image using the PhotoImage class
    # image = PhotoImage(file=image)
    # # Create a label to display the image
    # label = tk.Label(root, image=image)
    # # Pack the label to display it in the window
    # label.pack()
    # # Run the tkinter event loop
    Img = cv2.imread(image)
    cv2.imwrite(image, Img)
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)

# Defining Download() to download the video


def Download():

    # getting user-input Youtube Link
    Youtube_link = video_Link.get()

    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()

    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)

    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.get_highest_resolution()

    # Downloading the video to destination
    # directory
    videoStream.download(download_Folder)

    # Displaying the message
    messagebox.showinfo("SUCCESSFUL BRUH,",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)




# Creating object of tk class
root = tk.Tk()

# disabling the resizing property
root.geometry("550x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="#000112")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()
