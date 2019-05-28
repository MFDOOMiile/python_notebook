from datetime import date

"""
Notebook app

A note will have 3 parts:
- An ID
- Content
- Date/Time

"""
counter = 1
notebook = []
now = date.today()

while True:
    user_response = input("What would you like to do? \n"
                        "1. Add a note \n"
                        "2. Print a note \n"
                        "3. Exit \n")

    if user_response == "1":
        content = input("What is the note? \n> ")
        note_id = counter
        note = (note_id, str(now), content)
        notebook.append(note)
        counter += 1
        print(notebook)
    elif user_response =="2":
        for note in notebook:
            print(f"Id: {note[0]} | {note[2]}")
    elif user_response == "3":
        exit()
    else:
        print("Invalid input")



