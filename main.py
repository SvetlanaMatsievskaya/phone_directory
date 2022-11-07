from os.path import exists
from cvs_creation import create
from file_writing import write_scv
from file_writing import write_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    create()

write_scv()
write_txt()