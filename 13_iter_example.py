from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: float
    
def main() -> None:
    inventory = [
        Item("Laptop", 1.5),
        Item("Phone", 0.5),
        Item("Book", 1.0),
        Item("Camera", 1.0),
        Item("Headphone", 0.5),
        Item("Charger", 0.5)
    ]
    
    #inventory_iterator = inventory.__iter__()
    #inventory_iterator = iter(inventory)
    
    #print(inventory_iterator.__next__()) 
    #print(inventory_iterator.__next__()) 
    #print(next(inventory_iterator))
    #print(next(inventory_iterator)) 
    
    for item in inventory: # for uses the iter and next dunder methods
        print(item)
        
    with open("countries.txt") as file:
        for line in iter(file.readline, ""):
            print(line, end="")
    
if __name__ == '__main__':
    main()