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

while counter <= 5:
    content = input("What is the note? \n> ")
    note_id = counter
    note = (note_id, str(now), content)
    notebook.append(note)
    counter += 1
    print(notebook)

