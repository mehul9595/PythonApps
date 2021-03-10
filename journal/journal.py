import os
from pathlib import Path

def create_journal(journal_name):
    cwd = Path(".","data")
    # print(cwd)
    new_file = Path.joinpath(cwd, journal_name.rstrip() + ".txt")
    # print(new_file.exists())
    # print(Path.resolve(new_file))
    if new_file.exists() == False:
        new_file.touch()
        return "New {} created.".format(new_file.name)
    else:
        return "Journal already created!"
        
    # Path.joinpath(cwd, journal_name+".txt").touch()
    # print(journal_file)
    # print(Path(journal_file).is_file())
    # if Path(journal_file).is_file():
    #     return True
    # else:
    #     return False

def load_journal(name):
    data = []
    files = show_journals()
    path = Path(".","data")
    # files =  [e for e in path.iterdir() if e.is_file()] 

    file_number = int(input("Select Journal to load:"))
    selected_file = files[file_number - 1]
    print("Loading journal file:", selected_file.name)
    
    if selected_file.is_file(): 
        # content = filename.read_text() # to read full text of the file
        # print(content)
        with selected_file.open() as f:
            data = f.readlines()
            for index, l in enumerate(data):
                print("[{}*]".format(index+1), l.rstrip())

    # print(selected_file.exists())
    # print(selected_file)
    # print(selected_file.is_file())

def show_journals():
    current_path = Path(".","data")
    files = Path.iterdir(current_path)
    for index, file in enumerate(files):
        print("[{}] {}".format(index + 1, file.name))
    return [e for e in path.iterdir() if e.is_file()]

def add_entry(journal_name, data):
    journal_name = Path(journal_name)
    print(journal_name.is_file())