import os
from pathlib import Path

def create_journal(journal_name):
    cwd = Path(".","data")
    # print(cwd)
    new_file = Path.joinpath(cwd, journal_name.rstrip() + ".txt")
    # print(new_file.exists())
    # print(Path.resolve(new_file))
    if new_file.exists() == False:
        return new_file.touch()
        # print(new_file)
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
    filename = Path.joinpath(Path("."), "data", name)
    
    if filename.is_file(): 
        # content = filename.read_text() # to read full text of the file
        # print(content)

        with filename.open() as f:
            data = f.readlines()
            for l in data:
                print(l.rstrip())

    print(filename.exists())
    print(filename)
    print(filename.is_file())

# load("journal_data.txt")

def show_journals():
    current_path = Path(".","data")
    files = Path.iterdir(current_path)
    for p in files:
        print(p.name)