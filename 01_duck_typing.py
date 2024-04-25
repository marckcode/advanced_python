# structure typing: static, compares structures of objects when the code is compiled
# duck typing: dynamic, looks at parts that matter (Python)

# annotations (Python 3.9+)
my_str: str = "Hello World"
my_list: list[int] = [14, 12, 15, 15]
my_dict: dict[str, int] = {"one": 123, "two": 564, "three": 789}

len(my_str)    # 11
len(my_list)   # 4
len(my_dict)   # 3

class Book:
    def __init__(self, author: str, title: str, pages: int):
        self.author = author
        self.title = title
        self.pages = pages
        
    def __len__(self):
        return self.pages

b: Book = Book("Robert Martin", "Clean Code", 464)
print(len(b))