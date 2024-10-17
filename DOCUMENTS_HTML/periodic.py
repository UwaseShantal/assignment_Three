import periodictable
def atomic():
    while True:
        atomic_number=int(input("enter atomic number of element: "))

        if atomic_number==-1:
            break
        try:
            element= periodictable.elements[atomic_number]
            print("\nElement Information: ")
            print(f"Name: {element.name}")
            print(f"Mass: {element.symbol}")
            print(f"Atomic Number: {element.number}")
        except KeyError:
            print(f"not found")    
            


              
