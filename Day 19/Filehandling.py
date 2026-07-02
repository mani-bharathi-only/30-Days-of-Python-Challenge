import json

#Json to Dictionary
sam_jason='''{"Name":"Vinoth",
            "Age":"14",
            "Skills":["Python","Java","C"]
}'''
file=json.loads(sam_jason)
print(file["Name"],file["Age"],file["Skills"])


#Dictionary to JSON
animal={"lion":"King",
        "Elephant":"Strong"
       }

animal_json=json.dumps(animal,indent=2)
print(type(animal_json))
print(animal_json)