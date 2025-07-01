def open_file(file_name):
    try:
        with open(file_name,'r+', encoding='utf-8')as file:
            content = file.read()
            print("File Content:")
            print(content)
            file.write("The content is added to the file")
            file.write("\n the content is added successfully")
            file.write("\n dont over ride on my file\n")
    except PermissionError:
        print("Error: Permissison denied to open the file")
        
    except FileNotFoundError:
        print("Error: File not found")
    
        
file_name=input("Input a file name:")
open_file(file_name)