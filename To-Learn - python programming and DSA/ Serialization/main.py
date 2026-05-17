#serialization

#converting Python objects into transferable/storable format

#its helps in saving object ,transfer it through internet and store

#Python Object
#      ↓
#Serialization
#    ↓
#JSON / Bytes / File
#      ↓
#Deserialization
#      ↓
#Python Object


#Deserialization

#opposite process to reverse serialised data
#serialized format → Python object

#Common Serialization Formats

#json    ---- apis and webs
#csv     ---- tables
#pickle  ---- python objects
#yaml    ---- configs
#Protocol Buffers ---- high performance system

#json and pickle are most used and important ones


#JSON Serialization

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

with open("users.json", "w") as file:             # ------> file serialization
    json.dump(data, file,indent=4) #writes data to json files directly

#dumps() #-------> json string serialization
json_string = json.dumps(data) #converts a python object to a json string format not a file
print(json_string)


#reading json  ----> deserialize file

with open("users.json", "r") as file:
    data_dict = json.load(file) #reads file and creates an object
    print(data_dict)

    #accessing data from the object
    print(data_dict["users"][0]["name"])
    print(data_dict["users"][0]["age"])

#loads() ------> deserialize json string
py_object = json.loads(json_string) #converts json string into a python object
print(py_object)


#json dont understand or serialize custom python objects


#Pickle Serialization

#pickel serialize almost ANY Python object

import pickle

data = [1,2,3]

with open("data.pkl", "wb") as file:   #-----> wb ---> write binary --- pickle uses binary format

    pickle.dump(data, file)

#deserialize pickle
with open("data.pkl", "rb") as file:  #---->rb------> read binary

    data = pickle.load(file)

print(data)

#custom class
class Student:

    def __init__(self, name):
        self.name = name


s1 = Student("Aravind")

#serialization
with open("student.pkl", "wb") as file:

    pickle.dump(s1, file)


#Deserialization
with open("student.pkl", "rb") as file:

    student = pickle.load(file)

print(student.name)

#pickle files can be dangerous because it can carry executable code which can be dangerous


#Use JSON for:
#APIs
#frontend/backend communication
#configs
#web systems

#Use Pickle for:
#ML models
#Python internal systems
#complex Python objects





