meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
    
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No esta en nuestro diccionario")
    
    #meme_dict.get es un método de los diccionarios en Python que se utiliza 
    # para acceder al valor asociado a una clave específica. Es una forma segura de buscar 
    # una clave porque no genera un error si la clave no existe en el diccionario.
