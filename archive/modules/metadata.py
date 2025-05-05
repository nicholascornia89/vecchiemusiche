"""
This scripts reorganize and updates metadata from CSV files

- batch import from csvs
- create a JSON database
- clean up data

"""
import sys

sys.path.append("./modules")  # importing custom functions in modules
from modules.utilities import *

base_url = "https://vecchiemusiche.be/archive/"

# returns JSON database saved in metadata/database folder
def vm_old_archive_creation(metadata_path, data_path):
    vm_archive = {
        "manifestations": [],
        "collections": [],
        "composers": [],
        "poets": [],
        "patrons": [],
        "publishers": []
    }

    # get composers
    composers = csv2dict(os.path.join(metadata_path,"old_archive", "composers.csv"))
    for item in composers:
        vm_archive["composers"].append(
            {
                "full_name": item["name"],
                "last_name": item["last_name"],
                "wikidata_QID": item["wikidata_qid"],
                "RISM_ID": item["rism_id"],
                "manifestations": []
            }
        )
    # get poets
    poets= csv2dict(os.path.join(metadata_path,"old_archive", "poets.csv"))
    for item in poets:
    	query = list(filter(lambda x: x[1]["full_name"] == item["name"],enumerate(vm_archive["poets"])))
    	if len(query) == 0: # make new element
	        vm_archive["poets"].append(
	            {
	                "full_name": item["name"],
	                "last_name": item["last_name"],
	                "wikidata_QID": item["wikidata_qid"]
	                "manifestations": [item["manifestation"]]
	                
	            }
	        )
	    else:
	    	vm_archive["poets"][query[0][0]]["manifestations"].append(item["manifestation"])

	# get publisherse
	publishers= csv2dict(os.path.join(metadata_path,"old_archive", "publishers.csv"))
    for item in publishers:
    	query = list(filter(lambda x: x[1]["full_name"] == item["name"],enumerate(vm_archive["publishers"])))
    	if len(query) == 0: # make new element
	        vm_archive["publishers"].append(
	            {
	                "full_name": item["name"],
	                "last_name": item["last_name"],
	                "wikidata_QID": item["wikidata_qid"]
	                "collections": [item["collections"]]
	                
	            }
	        )
	    else:
	    	vm_archive["publishers"][query[0][0]]["manifestations"].append(item["manifestation"])



    # get manifestations
    manifestations = csv2dict(os.path.join(metadata_path,,"old_archive", "musical_pieces.csv"))
    for item in manifestations:
    	composer_query = list(filter(lambda x: x["full_name"] == item["composer"], vm_archive["composers"]))
    	if len(query) >0:
    		dirname = composer_query[0]["last_name"].replace(" ","_")+"|"+item["title"].replace(" ", "_")
	        vm_archive["manifestations"].append(
	            {
	                "title": item["title"],
	                "composer": item["composer"],
	                "directory_name": dirname,
	                "poet": "",
	                "patron": "",
	                "part_of": "",
	                "external_source": "",
	                "digital_asset": base_url+"/"+dirname+"/"+dirname".zip",
	                
	            }
	        )

    

    # export JSON database
    dict2json(
        vm_archive, os.path.join(metadata_path, "vm_archive-" + get_current_date()+".json")
    )

    return vm_archive
