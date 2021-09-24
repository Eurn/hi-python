import json
import os

file = "example.json"
if (os.path.exists(file)):
    with open('example.json', 'r') as file:
        file = json.loads(file.read())

    string = ""
    for cle in file.keys():
        string = string + "[" + cle + "]\n"
        elem = file[cle]
        for s_cle in file[cle].keys():
            string = string + s_cle + "=" + str(file[cle][s_cle]) + "\n"
        string = string + "\n"
    print(string)

    with open('example.ini', 'w') as file:
        file.write(string)

else:
    print("le fichier n'existe pas")
