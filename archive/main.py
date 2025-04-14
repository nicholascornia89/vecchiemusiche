"""
Main script to be runned
"""
import sys

sys.path.append("./modules")  # importing custom functions in modules
from modules.utilities import *
from modules.metadata import *
from modules.data import *

metadata_path = os.path.join("metadata")

data_path = os.path.join("data")


"""
Create directory structure
"""


vm_archive = vm_old_archive_creation(metadata_path, data_path)

create_vm_archive_directories(vm_archive)
