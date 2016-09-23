import json
import sys


def load_data(filepath):
    with open(filepath) as data_file:
    	data = json.loads(data_file.read())
    return data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=2))


if __name__ == '__main__':
	input_str = sys.argv[1]
	if input_str.lower().endswith('.json'):
		data = load_data(sys.argv[1])
		pretty_print_json(data)
	else:
		raise NameError('Wrong file type!')
    
