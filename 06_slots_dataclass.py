import timeit
from dataclasses import dataclass
from functools import partial
from statistics import median

@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str
    
@dataclass(slots=True) # uses slots instead of dictionaries
class PersonSlots:
    name: str
    address: str
    email: str
    
def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    person.address
    del person.address
    
def main():
    person = Person("Marck", "123 Main St", "marck@gmail.com")
    person_slots = PersonSlots("Marck", "123 Main St", "marck@gmail.com")
    no_slots = median(timeit.repeat(partial(get_set_delete, person), number=1000000))
    slots = median(timeit.repeat(partial(get_set_delete, person_slots), number=1000000))
    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvemente: {(no_slots - slots)*100 / no_slots: .2f} %")


if __name__ == '__main__':
    main()


 