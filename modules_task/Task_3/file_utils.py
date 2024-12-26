def read_file(file_path):
    try:
        with open(file_path,'r') as f:
            data=f.read()
            return data
    except FileNotFoundError as fn:
        return 'Please give a proper file name !!'

def write_file(file_path):
    with open(file_path,'w') as f:
        data=input('Enter your data :')
        f.write(data)


def append_to_file(file_path,content):
    with open(file_path,'a') as f:
        f.write(content)

