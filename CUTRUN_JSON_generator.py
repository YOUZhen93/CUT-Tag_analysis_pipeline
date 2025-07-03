import json
import sys

# Step 1: Read the template JSON file from command argument
template_file = sys.argv[1]
output_file = sys.argv[2]

with open(template_file, 'r') as file:
    template_data = json.load(file)

args = sys.argv[3:]
input_output = template_data.get("input_output", {})

for i in range(0, len(args)):
    key = args[i].split(":::")[0]
    value = args[i].split(":::")[1]
    input_output[key] = value

template_data["input_output"] = input_output


with open(output_file, 'w') as file:
    json.dump(template_data, file, indent=4)

print("New JSON file has been generated successfully.")
