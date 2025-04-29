import os  

def get_assets_working_dir():  
    assets_directory = os.getcwd()  
    full_directory = os.path.join(assets_directory, "assets")  
    path_for_style = full_directory.replace('\\', '/') + '/'  
    return path_for_style  

get_assets_working_dir()  