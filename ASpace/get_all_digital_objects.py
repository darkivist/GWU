import os, json

# This script downloads all digital objects by repository; requires ArchivesSnake

from asnake.client import ASnakeClient
client = ASnakeClient()
client.authorize()

def get_all_digital_objects(tar_dir,repo_num):
    all_ids = client.get('repositories/' + repo_num + '/digital_objects?all_ids=true').json()
    for digital_object_id in all_ids:
        newJSON = tar_dir + "/" + str(digital_object_id) + '.json'
        resource = client.get('repositories/' + repo_num + '/digital_objects/' + str(digital_object_id)).json()
        with open(newJSON, 'w') as outfile:
            json.dump(resource, outfile, sort_keys=True, indent=4)

tar_dir = input("Name of target directory: ")
repo_num = input("Repository number: ")
get_all_digital_objects(tar_dir,repo_num)
