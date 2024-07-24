traductor_dict = { 
            "freckle": "pecas",
            "laundry": "labadero",
            "skillully": "hábilmente",
            }
word = input("escribe una palabra en inglés)

if word in traductor_dict.keys():
    print(traductor_dict[word])
else:
    print("no tenemos esa palabra)
