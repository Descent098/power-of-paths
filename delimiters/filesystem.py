from __future__ import annotations # Allows type definitions to work properly

from string import ascii_uppercase             # All uppercase letters in a list
from dataclasses import dataclass              # Used to create classes faster
from typing import Literal, List, Union, Tuple # Used to type class attributes faster

# Forces a value to be an uppercase letter
UPPERCASE_LETTERS = Literal[ 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

@dataclass
class File:
    filename:str

@dataclass
class Folder:
    name: str
    contents: Union[List[Union[Folder, File]], None] = None # The contents of Folder
    

@dataclass
class Drive:
    letter: UPPERCASE_LETTERS # Forces a value to be an uppercase letter
    contents: Union[List[Union[Folder, File]], None] = None # The contents of drive

def find_folder(container:Union[Drive, Folder], folder_name:str) -> Folder:
    # Finds a folder in a specified container
    for item in container.contents:
        if type(item) == Folder:
            if item.name == folder_name:
                return item
    raise ValueError(f"Could not find folder {folder_name} in {container}")

def find_file(container:Union[Drive, Folder], file_name:str) -> File:
    # Finds a file in a specified container
    for item in container.contents:
        if type(item) == File:
            if item.filename == file_name:
                return item
    raise ValueError(f"Could not find file {file_name} in {container}")


def get_file(path: str, drives:List[Drive]):
    if not path[0] in ascii_uppercase:
        raise ValueError("Incorrect path provided")

    # Find correct drive
    correct_drive = None
    for drive in drives:
        if path[0].upper() == drive.letter:
            correct_drive = drive
            break # End loop
    
    if not correct_drive: # No drive with the letter was found
        raise ValueError(f"No drive with leter {path[0]} found")
    
    # Manipulate the path variable
    path = path[4:] # Remove drive information
    
    ## Assign variables for the loop
    filename = path.split("/")[-1] # Get just the filename
    folders = path.split("/")[:-1] # Get just the folders as a list of str's
    current_folder = find_folder(correct_drive, folders[0])
    folders.pop(0) # Remove first folder since it's the current_folder
    correct_file = None

    if not folders: # If the file is in the current directory/drive
        correct_file = find_file(current_folder, filename)

    # Loop over each folder to find the file
    for folder in folders:
        # Assign the current folder to the current piece of the path
        current_folder = find_folder(current_folder, folder)
        try:
            print(f"Checking {folder}")
            correct_file = find_file(current_folder, filename)
            break
        except ValueError:
            print(current_folder)

    print(correct_file)


# Testing
## Create files and folders

project_folder = Folder("project", [
    File("file.txt"),
    File("readme.md"),
    Folder("images", [
        File("lake.png")
    ])
])

## Create drive

c = Drive("C", [project_folder])


def search_folder(folder:Folder, filename:str) -> Tuple[str, Union[File,None]]:
    """Allows you to find a file in a folder based on filename

    Parameters
    ----------
    folder : Folder
        The folder to search

    filename : str
        The name of the file to find

    Returns
    -------
    Tuple[str, Union[File,None]]
        Returns the path, and File object if file exists, else returns blank string and None
    """
    path = f"/{folder.name}"
    result_file = None
    
    for content in folder.contents:
        if type(content) == Folder: 
            result_path, result_file = search_folder(content, filename)
            if result_path:
                path += f"{result_path}"
        else:
            if content.filename == filename:
                path += f"/{filename}"
                result_file = content
                break
    if not result_file:
        return "", None

    return path, result_file


def search_file(filename: str, drives:List[Drive]) -> Tuple[str, Union[File, None]]:
    """Find the absolute path of a file in any location based on filename

    Parameters
    ----------
    filename : str
        The file to search for

    drives : List[Drive]
        The drives to search in

    Returns
    -------
    Tuple[str, Union[File, None]]
        Returns the path to the file and the File object if exists, else if file does not exist return blank string and a None
    """
    for drive in drives:
        path = f"{drive.letter}:/"
        for contents in drive.contents:
            if type(contents) == Folder:
                result_path, file = search_folder(contents, filename)
                if result_path:
                    return f"{path}{result_path}", file
            else:
                if filename == contents.filename:
                    path += filename
                    return path, contents
    return "", None # Could not find file
            
if __name__ == "__main__": 
    print(get_file("C://project/images/lake.png", [c]))
    print(search_file("lake.png", [c]))
    print(search_file("lakse.png", [c]))
