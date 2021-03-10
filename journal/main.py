import journal, os
def print_header():
    print("""What you want to do today?: 
    [S]how Journals
    [N]ew Journal 
    [L]oad Journals
    [A]dd Journal Entry
    [D]elete Journal
    [Q]uit application
    [C]lear screen""")

def main():
    print("Let's play with journal's")
    print_header()
    cmd = -1
    while cmd != "q" and cmd:
        cmd = str(input("Enter a command:")).lower()

        if cmd == "s":
            journal.show_journals()
        elif cmd == "n":
            new_journal = input("New journal file name:")
            msg = journal.create_journal(new_journal)
            print(msg)
        elif cmd == "l":
            journal.load_journal()
        elif cmd == "a":
            print("adding entry to journal")
            files = journal.show_journals()
            choose_file = int(input("Select a file number:"))
            if len(files) >= choose_file:
                print("Enter data and press return when done:")
                str_content = str(input())
                journal.add_entry(files[choose_file - 1], str_content)
            else:
                print("Invalid file number, try again.")
        elif cmd == "d":
            files = journal.show_journals()
            choose_file = int(input("Select a file number to delete:"))
            if len(files) >= choose_file:
                journal.remove_file(files[choose_file - 1])
            else:
                print("Invalid file number, try again.")
        elif cmd == "q": 
            print("Bye! see you again.")        
        elif cmd == "c":
            cls()
            print_header()
        else:
            print("Invalid command!, please try again.")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
if __name__ == "__main__":
    main()