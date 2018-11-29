import os
import tempfile
import argparse
import json

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Key name")
    parser.add_argument("--value", help="Value", nargs="+")
    args = parser.parse_args()
    return args

def read_dict(storage_path):
    with open(storage_path) as f:
        my_dict = json.load(f)
    return my_dict

def write_dict(storage_path, my_dict):
    with open(storage_path, 'w') as f:
        json.dump(my_dict, f)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

args = get_arguments()
try:
    my_dict = read_dict(storage_path)
except Exception as e:
    my_dict = dict()

if args.value is None:
    try:
        #print(my_dict[args.key])
        print(', '.join(my_dict[args.key]))
    except Exception as e:
        print("None")
else:
    my_dict[args.key] = args.value
    write_dict(storage_path, my_dict)
