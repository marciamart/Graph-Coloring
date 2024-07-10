import json

data = []

with open('data.txt', 'r') as d:
    for line in d:

        instance, vertex, edge, x, source = line.split()
        chromatic_number = x if x == '?' else int(x)

        data.append(
            {
                'instance': instance,
                'vertex': int(vertex),
                'edge': int(edge),
                'chromatic number': chromatic_number,
                'source': source
            }
        )

with open('dados.json', 'w') as j:
    json.dump(data, j, indent=4)
    print(data)