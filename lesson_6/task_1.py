# Aceeasta este prima sarcină a aceestei lecții și este legată de dicționare.
# Creați un dicțioar gol
# CODUL TĂU VINE MAI JOS:
my_dict = dict()
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "name" și valoarea fiind "John"
# CODUL TĂU VINE MAI JOS:
my_dict['name'] = 'John'
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "age" și valoarea fiind 30
# CODUL TĂU VINE MAI JOS:
my_dict['age'] = 30
# CODUL TĂU VINE MAI SUS:

# Acum afișați dicționarul
# CODUL TĂU VINE MAI JOS:
print(f'"my_dict" contains: {my_dict}')
# CODUL TĂU VINE MAI SUS:

# Acum ștergeți cheia "name" din dicționar
# CODUL TĂU VINE MAI JOS:
del my_dict['name']
# CODUL TĂU VINE MAI SUS:

# Acum afișați dicționarul
# CODUL TĂU VINE MAI JOS:
print(f'"my_dict" contains: {my_dict}')
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "city" și valoarea fiind "New York" folosind metoda setdefault()
# CODUL TĂU VINE MAI JOS:
my_dict.setdefault('city', 'New York')
# CODUL TĂU VINE MAI SUS:

# Afișați toate cheile din dicționar 
# CODUL TĂU VINE MAI JOS:
print(f'"my_dict" all keys: {my_dict.keys()}')
# CODUL TĂU VINE MAI SUS:

# Afișați toate valorile din dicționar
# CODUL TĂU VINE MAI JOS:
print(f'"my_dict" all values: {my_dict.values()}')
# CODUL TĂU VINE MAI SUS:

# Afișați toate perechile de cheie-valoare din dicționar folosind metoda items()
# CODUL TĂU VINE MAI JOS:
print(f'"my_dict" all keys and values: {my_dict.items()}')
# CODUL TĂU VINE MAI SUS:

# Afișați numărul de perechi de cheie-valoare din dicționar
# CODUL TĂU VINE MAI JOS:
print(f'"my_dict" number of all keys and values pairs: {len(my_dict)}')
# CODUL TĂU VINE MAI SUS:

# Extrageți valoarea unei chei inexistente fără a genera o eroare
# CODUL TĂU VINE MAI JOS:
print(f'Extracting a non-existing value from "my_dict" without generating an error: {my_dict.get("lastname")}')
print(f'Extracting a non-existing value from "my_dict" without generating an error: {my_dict.get("lastname", "N/A")}')
# CODUL TĂU VINE MAI SUS:

# Acum actualizați dicționarul cu un alt dicționar, folosind metoda update()
# CODUL TĂU VINE MAI JOS:
my_dict2 = {'country': 'USA'}
my_dict.update(my_dict2)
# CODUL TĂU VINE MAI SUS:

# Setați valoarea cheii "pizza" la 10 folosind metoda setdefault()
# CODUL TĂU VINE MAI JOS:
my_dict.setdefault('pizza', 10)
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul
# CODUL TĂU VINE MAI JOS:
print(f'After update() and setdefault() "my_dict" contains: {my_dict}')
# CODUL TĂU VINE MAI SUS:

# Ștergeți cheia "pizza" din dicționar folosind metoda pop()
# CODUL TĂU VINE MAI JOS:
my_dict.pop('pizza')
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul
# CODUL TĂU VINE MAI JOS:
print(f'After pop() "my_dict" contains: {my_dict}')
# CODUL TĂU VINE MAI SUS:

# Ștergeți toate perechile de cheie-valoare din dicționar 
# CODUL TĂU VINE MAI JOS:
my_dict.clear()
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul
# CODUL TĂU VINE MAI JOS:
print(f'After clear() "my_dict" contains: {my_dict}')
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de dicționare