"""
This script is concerned with batch import of files, like images and scores.
"""
import sys

sys.path.append("./modules")  # importing custom functions in modules
from modules.utilities import *


# create directories with for title.replace(" ","_")+"|"+composer.replace(" ","_")
def create_vm_archive_directories(vm_archive):
    base_path = os.path.join("data")
    # create directories based on title and composer
    for piece in vm_archive["manifestations"]:
        dirname = piece["directory_name"]
        os.makedirs(os.path.join(base_path, dirname), exist_ok=True)
