import json

def create_json_tree(data, level=0, node=None):
    if node is None:
        node = {'name': 'marca', 'children': []}
    i = 0
    while i < len(data):
        parts = data[i].split('.')
        current_level = int(parts[0])
        if current_level == level:
            node['children'].append({'name': parts[-1].strip(), 'children': []})
            i += 1
        elif current_level > level:
            node['children'][-1] = create_json_tree(data[i:], current_level, node['children'][-1])
            i += 1
        else:
            return node
    return node


# Read the topic structure from the file
with open("mapamental.txt", "r") as f:
    topic_structure = f.read().split("\n")

# Create the JSON tree
tree_data = create_json_tree(topic_structure)

# Write the JSON tree to a file
with open("var.js", "w") as f:
 f.write("var treeData = ")
 json.dump(tree_data, f)
 f.write(";")
