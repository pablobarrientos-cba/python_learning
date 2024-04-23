# same folder or a different one
# with opens and close the file after usage 
# SYNTAX> with open("filename.txt", "r") as my_file:
# r (read) / w (write) / a (append) 
# + (add a second mode to w or a in order to read as well) / w+

with open("frases.txt") as phrases:
    for line in phrases:
        print("--- Phrase ---")
        print(line)

notes = {
    "Josefina": 99,
    "Candelaria": 93,
    "Silvana": 90
}

with open("data_notes.txt", "a") as note_file:
    for name, score in notes.items():
        note_file.write(name + " got a score of: " + str(score) + " in English test\n")