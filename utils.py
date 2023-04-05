import os, platform
import sqlite3
from tkinter import font
import tkinter as tk
import hashlib

PLATFORM = platform.uname().system

if PLATFORM == "Windows":
    CLR_CMD = "cls"
elif PLATFORM == "Linux":
    CLR_CMD = "clear"
    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "masterDataBase.db")

def create_connection(): 
    connection = None
    try:
        connection = sqlite3.connect(DB_FILE)
    except sqlite3.Error as e:
        print(f"The Error '{e}' occurred.")
    return connection

def database_handler(function):
    def wrapper():

        with create_connection() as conn:
            return function(db=conn)

    return wrapper

def hash_data(data, hash_func=None):
    return hashlib.sha256(data.encode()).hexdigest()

def change_frame(frame_1, frame_2):
    frame_1.pack(fill="both", expand=1)
    frame_2.pack_forget()
    frame_1.tkraise()

def clrscr(): os.system(CLR_CMD)

def pack_frame(frame):
    for child in frame.winfo_children():
        child.pack()


if __name__ == "__main__":
    print(hash_data("Hello World"))