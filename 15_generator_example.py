from typing import Generator


def simple_generator() -> Generator[str, None, None]:
    generator_str = "Hello World"
    yield generator_str
    
    generator_str += "!"
    yield generator_str
    

def main() -> None:
    for generator_str in simple_generator():
        print(generator_str)
        

if __name__ == "__main__":
    main()