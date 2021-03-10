import journal

def main():
    print("Let's play with journal's")
    print("Commands: [1] Show Journals, [2] Create Journal [3] Load Journal, [4] Quit the application")
    cmd = 0    
    while cmd != 4:
        cmd = int(input("Enter a command:"))
        if cmd == 1:
            journal.show_journals()
        elif cmd == 2:
            new_journal = input("New journal file name:")
            msg = journal.create_journal(new_journal)
            print(msg)
        elif cmd == 3:
            print("Thanks!")
        elif cmd == 4: 
            print("Bye! see you again.")
        else:
            print("invalid command!")
    
if __name__ == "__main__":
    main()