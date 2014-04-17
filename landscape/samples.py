import csv, os, itertools
import requests
import hashlib

resources = {
    'Keywords': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=12',
    'UK': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=0',
    'Georgia': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=1',
    'Canada': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=2',
    'Mexico': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=10',
    'EU': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=11',
    'Moldova': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=15',
    'UNOPS': 'https://docs.google.com/spreadsheet/ccc?key=0AvMxyqIb0BZfdEdjdnVWc0ZLeERCeDNERVRiRTVXZkE&output=csv&gid=14',
}

name_key = "English Name"
phase_key = "Phase"
entity_key = "Entity"

def get_resource(name, cache=True):
    url = resources[name]
    path = '.cache/%s.csv' % name
    if cache and os.path.exists(path):
        with open(path) as o:
            return csv.reader( o.read().split('\n') )
    else:
        response = requests.get(resources[name])
        assert response.status_code == 200, 'Cannot access resource'
        if not os.path.exists('.cache'):
            os.mkdir('.cache')
        with open(path, 'w') as o:
            o.write( response.content )
        return csv.reader(response.content.split('\n'))

def get_data(name, cache=True):
    rows = get_resource(name, cache=cache)
    header = None
    data = []
    for row in rows:
        if header:
            data.append( dict(zip(header, row)) )
        else:
            header = row
    return data

def set_of_values(s):
    result = set()
    for s in name_key.split(','):
        s = s.strip()
        if s:
            result.add()

def get_entities(line):
    entities = line[entity_key] or '?'
    entities = set([x.strip() for x in entities.split(',') if x.strip()])
    return entities

def load_samples(names, cache=True):
    samples = []
    for name in names:
        data = get_data(name, cache=cache)
        last_name = None
        for line in data:
            header = line[name_key] or last_name
            last_name = header
            for entity in get_entities(line):
                samples.append({'header': header, 'entity': entity, 'sample': name})
    return samples

def load_headers(name, cache=True):
    results = []
    for line in get_data(name, cache=cache):
        if line[name_key]:
            results.append(line[name_key])
    return results
