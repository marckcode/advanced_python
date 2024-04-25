import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

#@dataclass(kw_only=True)
#@dataclass(frozen=True)
@dataclass
class Person:
    name: str
    address: str
    id: str = field(default_factory=generate_id, init=False)
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    _search_string: str = field(init=False, repr=False)
    
    @property
    def search_string(self) -> str:
        return f"{self.name}{self.address}"
    
    def __str__(self) -> str: # overrides repr
        return self.name
    
def main() -> None:
    person = Person(name="John", address="123 Main St") 
    print(f"{person!r}")
    print(person.search_string)
    
if __name__ == '__main__':
    main()