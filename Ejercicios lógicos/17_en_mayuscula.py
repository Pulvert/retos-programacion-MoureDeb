"""
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""
def capital (string):

    list_phrase = []

    for i in string.split():
        list_phrase.append(i.capitalize())
        
    phrase = " ".join(list_phrase)

    print(phrase)
   
capital("La niña no se dejó peinar")