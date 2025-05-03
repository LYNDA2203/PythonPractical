#getting the value for 2d array
def read_2d_array(rows, cols, data_type):
    array = []

    print(f"Enter {rows * cols} values ({data_type}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = input()
            if data_type == 'int':
                row.append(int(value))
            elif data_type == 'float':
                row.append(float(value))
            elif data_type == 'bool':
                row.append(value.lower() in ['true', '1'])
            else:
                raise ValueError("Unsupported data type.")
        array.append(row)
    return array


def print_2d_array(array):
    print("2D Array Output:")
    for row in array:
        print(' '.join(str(val) for val in row))


def main():
    rows = int(input("Enter number of rows (M): "))
    cols = int(input("Enter number of columns (N): "))
    
    print("Choose data type: int / float / bool")
    data_type = input("Enter data type: ").strip().lower()

    array = read_2d_array(rows, cols, data_type)
    print_2d_array(array)


if __name__ == "__main__":
    main()
/*

PS C:\Users\Janci L\Desktop\princy study\python\com.bridgelabz.functionalPrograms> py 2DArray_read_print.py
Enter number of rows (M): 2
Enter number of columns (N): 3
Choose data type: int / float / bool
Enter data type: int
Enter 6 values (int):
2
3
4
5
7
8
2D Array Output:
2 3 4
5 7 8*/
    
    