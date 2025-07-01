def file_not_found(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            contents=file.readlines()
            print("File Content:")
            print(contents)
    except FileNotFoundError:
        print("Error: File not found.")
        
file_name = input("Input a file name:")
file_not_found(file_name)