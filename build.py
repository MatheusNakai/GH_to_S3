import os
import shutil

def build():

    #create venv
    os.system("python -m venv venv; source venv/bin/activate; pip install -r lambda_function/requirements.txt; mkdir upload ; cp lambda_function\gh_to_s3.py venv\lib\python3.8\site-packages")

#     #activate venv
#     os.system("")

#     #install requirements
#     os.system("")

#     #create dir upload
#     os.system("")

#     #copy gh_to_s3 to venv\lib\site-packages
#     os.system("")

    #zip venv\lib\site-packages to upload\function.zip
    shutil.make_archive("upload/function", "zip", "venv/lib/python3.8/site-packages") 

    return "upload"
