def open_file(file_name):
    encoding=input("Input the coding(ASCII,UTF-16,UTF-8)for the file:")
    try:
        with open(file_name,'r',encoding=encoding) as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        print("Error: Encoding issue occurred while reading the file.{encoding}")
file_name = input("Input the file name: ")
open_file(file_name)