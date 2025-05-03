def find_zero_sum_triplets(arr):
    n = len(arr)
    triplets = set()  # To store unique triplets

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = tuple(sorted((arr[i], arr[j], arr[k])))
                    triplets.add(triplet)

    return triplets


def main():
    n = int(input("Enter number of integers (N): "))
    print(f"Enter {n} integers:")
    arr = [int(input()) for _ in range(n)]

    result = find_zero_sum_triplets(arr)
    
    print(f"\nNumber of distinct triplets: {len(result)}")
    print("Distinct triplets that sum to 0:")
    for triplet in sorted(result):
        print(triplet)


if __name__ == "__main__":
    main()

/*

PS C:\Users\Janci L\Desktop\princy study\python\com.bridgelabz.functionalPrograms> py SumOfThreeInteger.py
Enter number of integers (N): 6
Enter 6 integers:
2
-1
-1
2
0
-2

Number of distinct triplets: 2
Distinct triplets that sum to 0:
(-2, 0, 2)
(-1, -1, 2)*/