# static: happens at compile or interprete time. (Java)
# dynamic: happens at run time.  (Python)

# manifest: explicit specify the type of the variable (C, Java)
# inferred: the type is inferred from the value (python)

def main() -> None:
    x = 'Hello ' + str(5)
    print(x)
    
if __name__ == "__main__":
    main()

