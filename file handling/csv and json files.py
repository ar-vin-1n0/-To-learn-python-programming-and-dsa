#CSV - COMMA SEPARATED VALUES

#csv stores table like data separated by commas
#eg name,age,city = aravind,20,tvm

import csv

#writing csv

#csv.writer()

rows = [
    ["Aravind", 20],
    ["Alex", 22]
]

#basic way to write csv
with open("new.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name","Age"]) #writes rows line by line
    writer.writerows(rows) #writes rows all at once


#advanced recommended way to write csv
#DictWriter is more good because it uses key value pairs to write and is much cleaner
data = [
    {
        "name": "Aravind",
        "age": 20,
        "city": "Kochi"
    },
    {
        "name": "Alex",
        "age": 22,
        "city": "Delhi"
    }
]

headers = ["name", "age", "city"] #headers for the csv

with open("user.csv", "w", newline="") as file: #newline to write each rows in a newline

    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader() #assign headers to orders from headers

    writer.writerows(data) #writes rows from data and assign each value to the key header


#reading csv

#csv.reader()

#basic csv reading
with open("user.csv", "r") as file:

    reader = csv.reader(file) #reader object
    next(reader)  #skips headers

    for row in reader: #loops through row by row
        print(row)


#DictReader()

#advanced and recommended way of csv reading
with open("user.csv", "r") as file:

    reader = csv.DictReader(file) #dictreader object

    for row in reader:
        print(row)#output in a dictionary based way like key value pairs
        print(row["name"]) #give specific rows
        age = int(row["age"]) #csv coverts everything into string so to use values convert it into right data type


#JSON -JAVASCRIPT OBJECT NOTATIONS

#text based data format used to store and transfer data
#similar to  python dictionary

import json

#writing json
data = {
    "users": [
        {
            "name": "Aravind",
            "age": 20
        },
        {
            "name": "Alex",
            "age": 22
        }
    ]
}

with open("users.json", "w") as file:
    json.dump(data, file,indent=4) #writes data to json files directly

#dumps()
json_string = json.dumps(data) #converts a python object to a json string format not a file
print(json_string)


#reading json

with open("users.json", "r") as file:
    data_dict = json.load(file) #reads file and creates an object
    print(data_dict)

    #accessing data from the object
    print(data_dict["users"][0]["name"])
    print(data_dict["users"][0]["age"])

#loads()
py_object = json.loads(json_string) #converts json string into a python object
print(py_object)


