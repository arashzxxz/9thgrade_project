import os  

def get_assets_working_dir():  
    assets_directory = os.getcwd()  
    full_directory = os.path.join(assets_directory, "assets")
    print(full_directory)
    return full_directory