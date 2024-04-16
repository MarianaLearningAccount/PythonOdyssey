# Aceasta este a doua ta sarcină legată de seturi
# Creați un set gol numit `numbers_set`
# CODUL TĂU VINE MAI JOS:
numbers_set = set()
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numerele de la 1 la 5 în setul `numbers_set`
# CODUL TĂU VINE MAI JOS:
for i in range(1, 6):
    numbers_set.add(i)
# CODUL TĂU VINE MAI SUS:

# Acum afișați setul `numbers_set`
# CODUL TĂU VINE MAI JOS:
print(f'"numbers_set" contains: {numbers_set}')
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numărul 6 la setul `numbers_set`
# CODUL TĂU VINE MAI JOS:
numbers_set.add(6)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în setul `numbers_set` folosind metoda update()
# CODUL TĂU VINE MAI JOS:
numbers_set.update(range(1, 6))
print(f'After update() "numbers_set" contains: {numbers_set}')
# CODUL TĂU VINE MAI SUS:

# Extrageți numărul 3 din setul `numbers_set`
# CODUL TĂU VINE MAI JOS:
numbers_set.remove(3)
# CODUL TĂU VINE MAI SUS:

# Ștergeți un număr inexistent din setul `numbers_set` fără a genera o eroare
# CODUL TĂU VINE MAI JOS:
numbers_set.discard(10)
print(f'After discard(10) "numbers_set" contains: {numbers_set}')
# CODUL TĂU VINE MAI SUS:

# Verificați dacă numărul 3 există în setul `numbers_set`
# CODUL TĂU VINE MAI JOS:
print(f'Check if 3 is present in "numbers_set": {3 in numbers_set}')
# CODUL TĂU VINE MAI SUS:

# Verificați elementele comune din setul `numbers_set` și setul {4, 5, 6, 7}
# CODUL TĂU VINE MAI JOS:
print(f'Elements present in both "numbers_set" and set {4, 5, 6, 7}: {numbers_set.intersection({4, 5, 6, 7})}')
# CODUL TĂU VINE MAI SUS:

# Verificați elementele diferite din setul `numbers_set` și setul {4, 5, 6, 7}
# CODUL TĂU VINE MAI JOS:
print(f'Elements not present in both "numbers_set" and set {4, 5, 6, 7}: {numbers_set.difference({4, 5, 6, 7})}')
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un subset al setului {1, 2, 3, 4, 5, 6, 7}
# CODUL TĂU VINE MAI JOS:
print(f'Check if "numbers_set" is subset of set {1, 2, 3, 4, 5, 6, 7}: {numbers_set.issubset({1, 2, 3, 4, 5, 6, 7})}')
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un subset al setului `numbers_set`
# CODUL TĂU VINE MAI JOS:
print(f'Check if set {{1, 2, 3, 4, 5, 6, 7}} is a subset of "numbers_set": { {1, 2, 3, 4, 5, 6, 7}.issubset(numbers_set) }')
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un superset al setului {1, 2, 3, 4, 5, 6, 7}
# CODUL TĂU VINE MAI JOS:
print(f'Check if "numbers_set" is superset of set {1, 2, 3, 4, 5, 6, 7}: {numbers_set.issuperset({1, 2, 3, 4, 5, 6, 7})}')
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un superset al setului `numbers_set`
# CODUL TĂU VINE MAI JOS:
print(f'Check if set {{1, 2, 3, 4, 5, 6, 7}} is a superset of "numbers_set": { {1, 2, 3, 4, 5, 6, 7}.issuperset(numbers_set) }')
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea setului `numbers_set`
# CODUL TĂU VINE MAI JOS:
print(f'Set "numbers_set" length: {len(numbers_set)}')
# CODUL TĂU VINE MAI SUS:

# Ștergeți toate elementele din setul `numbers_set`
# CODUL TĂU VINE MAI JOS:
numbers_set.clear()
# CODUL TĂU VINE MAI SUS:

# Afișați setul `numbers_set` pentru a verifica dacă a fost șters
# CODUL TĂU VINE MAI JOS:
print(f'After clear() "numbers_set" contains: {numbers_set}')
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru a doua ta sarcină legată de seturi