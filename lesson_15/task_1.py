# Aceasta este sarcina pentru lecția despre polimorfism, metode speciale și compoziție a claselor în Python.

from sigmoid_check.python_odyssey.lesson_15.lesson_15 import Lesson15

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.8
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.8

# VERIFICATION PROCESS
session = Lesson15()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE
După toată munca depusă pentru proiectul de la DARWIN și TechSolutions, ai primit o ofertă de la cei de la Microsoft, 
aceștia lucrează la crearea unui algoritm care le va permite procesarea a unor cantități mari de date.
"""

"""
Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și manipularea datelor într-un mod mai simplu
și eficient. Trebuie să creezi o clasă nouă `DataContainer`. Pentru a manipula datele vom folosi metodele speciale ale clasei.

Clasa va primi ca parametru o listă de numere integer.
- __init__ initializează clasa cu lista de numere.
- __str__ va returna lista de numere sub formă de string.
- __len__ va returna numărul de elemente din listă.
- __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
- __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
- __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
"""

# CODUL TĂU VINE MAI JOS:
class DataContainer:
    def __init__(self, lista_de_numere):
        self.lista_de_numere = lista_de_numere

    def __str__(self):
        return str(self.lista_de_numere)

    def __len__(self):
        return len(self.lista_de_numere)

    def __getitem__(self, index):
        return self.lista_de_numere[index]

    def __setitem__(self, index, value):
        self.lista_de_numere[index] = value

    def __add__(self, other):
        if isinstance(other, DataContainer):
            combined_data = self.lista_de_numere + other.lista_de_numere
            return DataContainer(combined_data)
        else:
            raise TypeError("Operatia de adaugare este permisa doar intre doua instante DataContainer.")
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(DataContainer))
# VERIFICATION PROCESS

"""
Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
- `SumaContainer` va calcula suma elementelor din listă.
- `ProdusContainer` va calcula produsul elementelor din listă.
Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
"""

# CODUL TĂU VINE MAI JOS:
class SumaContainer(DataContainer):
    def calculate(self):
        return sum(self.lista_de_numere)


class ProdusContainer(DataContainer):
    def calculate(self):
        produs = 1
        for num in self.lista_de_numere:
            produs *= num
        return produs
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(SumaContainer, ProdusContainer, DataContainer))
# VERIFICATION PROCESS

"""
Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `__call__` va returna o listă cu valorile maxime ale fiecărui container.
"""

# CODUL TĂU VINE MAI JOS:
class DataAnalysis:
    def __init__(self, lista_de_obiecte):
        self.lista_de_obiecte = lista_de_obiecte

    def add_container(self, container):
        self.lista_de_obiecte.append(container)

    def __call__(self):
        return [max(container.lista_de_numere) for container in self.lista_de_obiecte]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(DataAnalysis, DataContainer))
# VERIFICATION PROCESS

"""
Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `mean` va returna media aritmetică a elementelor din toate containerele.
- `median` va returna mediana elementelor din toate containerele.
- `min` va returna valoarea minimă din toate containerele.
- `sum` va returna suma elementelor din toate containerele.
"""

# CODUL TĂU VINE MAI JOS:
class DataStatistics:
    def __init__(self, lista_de_obiecte):
        self.lista_de_obiecte = lista_de_obiecte

    def add_container(self, container):
        self.lista_de_obiecte.append(container)

    def mean(self):
        total_sum = sum(sum(container.lista_de_numere) for container in self.lista_de_obiecte)
        total_len = sum(len(container) for container in self.lista_de_obiecte)
        return total_sum / total_len if total_len != 0 else 0

    def median(self):
        all_data = [item for container in self.lista_de_obiecte for item in container.lista_de_numere]
        sorted_data = sorted(all_data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]

    def min(self):
        all_data = [item for container in self.lista_de_obiecte for item in container.lista_de_numere]
        return min(all_data) if all_data else None

    def sum(self):
        total_sum = sum(sum(container.lista_de_numere) for container in self.lista_de_obiecte)
        return total_sum
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(DataStatistics, DataContainer))
# VERIFICATION PROCESS

"""
Iar pe ultima sută de metri, Microsoft a cerut și un element de filtrare a datelor.

Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
- `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
- `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
- `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a tuturor elementelor calculate cu metoda `mean` din clasa `DataStatistics`.
"""

# CODUL TĂU VINE MAI JOS:
class DataFilter:
    def __init__(self, lista_de_obiecte):
        self.lista_de_obiecte = lista_de_obiecte

    def add_container(self, new_container):
        self.lista_de_obiecte.append(new_container)

    def filter_zeros(self):
        return [num for container in self.lista_de_obiecte for num in container.lista_de_numere if num != 0]

    def filter_negatives(self):
        return [num for container in self.lista_de_obiecte for num in container.lista_de_numere if num < 0]

    def filter_positives(self):
        return [num for container in self.lista_de_obiecte for num in container.lista_de_numere if num >= 0]

    def filter_under_mean(self):
        stats = DataStatistics(self.lista_de_obiecte)
        mean = stats.mean()
        return [num for container in self.lista_de_obiecte for num in container.lista_de_numere if num > mean]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task_5(DataFilter, DataStatistics, DataContainer))
print(session.get_completion_percentage())
# VERIFICATION PROCESS