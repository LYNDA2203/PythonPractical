import sys
import math

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Please provide exactly two integer arguments: x and y")
        return

    # Parse command-line arguments
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    # Compute Euclidean distance using Math.pow
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    # Output the result
    print(f"Distance from ({x}, {y}) to (0, 0) is: {distance}")

if __name__ == "__main__":
    main()

/*
PS C:\Users\Janci L\Desktop\princy study\python\com.bridgelabz.functionalPrograms> py distance.py 4 5
Distance from (4, 5) to (0, 0) is: 6.4031242374328485
*/