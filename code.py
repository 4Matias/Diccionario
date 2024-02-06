meme_dict = {""
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL":"Una respuesta a una broma", 
            "SHEESH":"Ligera desaprobación",
            "CREEPY":"Algo aterrador o siniestro",
            "AGGRO":"Ponerse agresivo/enojado",
            }

P = input("Escribe una palabra que no entiendas:" )

if P in meme_dict.keys() :
    print(meme_dict[P])
    
else:
    print("No existe.")
