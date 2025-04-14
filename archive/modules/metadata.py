"""
This scripts reorganize and updates metadata from CSV files

- batch import from csvs
- create a JSON database
- clean up data

"""
import sys

sys.path.append("./modules")  # importing custom functions in modules
from modules.utilities import *


# returns JSON database saved in metadata/database folder
def vm_old_archive_import(old_archive_path):
