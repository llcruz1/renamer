# Function to rename multiple files 
import os
from os import path
from os import rename
from os import listdir
from os.path import splitext

def menu():
    option = int(input("""What do you want to do?
        1. Insert string at beginning
        2. Insert string at the end
        3. Insert string at given position
        4. Remove string at given position 
        5. Order files with numbered prefixes. Ex: 001.filename1, 002.filename2
        6. Exit\n"""))
    return option

def insert_beginning(path_to_file):
        string_insert = str(input("Type what to insert: "))
        for filename in (sorted(listdir(path_to_file))):
            name, ext = splitext(filename)
            dest = string_insert + name + ext
            rename(path_to_file + filename, path_to_file + dest)
        print("String inserted at the beginning of all files.\n")

def insert_end(path_to_file):
        string_insert = str(input("Type what to insert: "))
        for filename in (sorted(listdir(path_to_file))):
            name, ext = splitext(filename)
            dest = name + string_insert + ext
            rename(path_to_file + filename, path_to_file + dest)
        print("String inserted at the end of all files.\n")

def insert_position(path_to_file):
        string_insert = str(input("Type what to insert: "))
        position = int(input("Type de index to insert at (starts at 0):"))

        for filename in (sorted(listdir(path_to_file))):
            dest = filename[:position] + string_insert + filename[position:]
            rename(path_to_file + filename, path_to_file + dest)
        print("String inserted at index {} of all files.\n".format(position))

def remove_position(path_to_file):
        print("Remove from interval [start:end-1]: ")
        start = int(input("Start: "))
        end = int(input("End: "))

        for filename in (sorted(listdir(path_to_file))):
            dest = filename[0:start] + filename[end:]
            rename(path_to_file + filename, path_to_file + dest)
        print("String from index [{}:{}] removed from all files.\n".format(start,end))

def order_prefix(path_to_file):
        print("\nPad prefix with 0s: \nEx: 3 = 001,002,... , 2 = 01,02,...\n")
        pad = int(input("Pad: "))
        for count, filename in enumerate(sorted(listdir(path_to_file))):
            z_count = str(count+1).zfill(pad)
            name, ext = splitext(filename)
            dest = z_count + "." + name + ext
            rename(path_to_file + filename, path_to_file + dest)
        print("Files ordered by prefix.\n")


def switch(option, path_to_file):
    print(option)
    if option==1: 
        insert_beginning(path_to_file)
    elif option==2:
        insert_end(path_to_file)
    elif option==3:
        insert_position(path_to_file)
    elif option==4:
        remove_position(path_to_file)
    elif option==5:
        order_prefix(path_to_file)

def main():
    path_to_file = input("Full path to directory: ")
    option=0

    if path.exists(path_to_file):
        if not path_to_file.endswith("/"):
            path_to_file = path_to_file + "/"
        while option != 6:       
            option = menu()
            switch(option, path_to_file)
    else:
        print("\nPath not found.\n")    
    
      
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
