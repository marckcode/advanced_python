from dataclasses import dataclass
import itertools

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
    
    print("Count method")
    for i in itertools.count(10, 5): # number, steps
        print(i)
        if i == 50:
            break
    
    print("Repeat method")
    for i in itertools.repeat(10, 5): # repeat 10, 5 times
        print(i)
    
    print("Accumulate method") 
    subtotals = [2, 5, 7, 5, 3, 3]
    for i in itertools.accumulate(subtotals): # partial sums
        print(i)
        
    print("Permutation & Combination methods") 
    playing_cards: list[str] = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
    ]
    simple_list: list[str] = [
        "a", "b", "c"
    ]
    perms = itertools.permutations(playing_cards, 4) # order matters
    #for perm in perms:
        #print(perm)
        
    perms = itertools.combinations(simple_list, 2) # order does not matter
    for perm in perms:
        print(perm)
        
    print("Chain method")
    perms = itertools.chain(simple_list, ["d", "e", "f"])
    print(list(perms))
    
    print("Filterfalse method")
    print(list(itertools.filterfalse(lambda x: x.weight < 1, inventory)))
        
    print("Starmap method")
    print(list(itertools.starmap(lambda x, y: x * y, [(2, 6), (8, 4), (5, 3)])))
    
if __name__ == '__main__':
    main()