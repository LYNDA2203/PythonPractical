def keyboard_interrupts(n):
    try:
        print("You have entered:",n)
    
    except KeyboardInterrupt:
        print("input canceled by the user")

n=int(input("Enter the number:"))
keyboard_interrupts(5)
