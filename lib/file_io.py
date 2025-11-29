def write_file(file_name, file_content):
    the_file_name=f"{file_name}.txt"
    with open(the_file_name , "w") as file:
        file.write(file_content)
    pass

def append_file(file_name, append_content):
    full_name=f"{file_name}.txt"

    with open(full_name,"a") as file:
        file.write(append_content)
    pass

def read_file(file_name):
    full_name=f"{file_name}.txt"
    with open(full_name ,"r") as file:
        return file.read()
    pass
