import json
import sys


def load_data(filepath):
    with open(filepath) as data_file:
    	data = json.loads(data_file.read())
    return data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=2))


if __name__ == '__main__':
	input_parameter = sys.argv[1]
	if input_parameter.lower().endswith('.json'):
		json_data = load_data(input_parameter)
		pretty_print_json(json_data)
	else:
		raise NameError('Wrong file type!')
    
