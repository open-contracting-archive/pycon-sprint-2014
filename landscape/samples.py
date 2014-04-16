import csv, os
import requests
import hashlib

resources = {
    'UK': 'https://docs.google.com/spreadsheet/ccc?key=0AqLP9fZSKM8jdFg2WGhHQi1QbE54Wml5aDNyaUVDRGc&output=csv&gid=0',
    'Canada': 'https://docs.google.com/spreadsheet/ccc?key=0AqLP9fZSKM8jdFg2WGhHQi1QbE54Wml5aDNyaUVDRGc&output=csv&gid=2',
    'Mexico': 'https://docs.google.com/spreadsheet/ccc?key=0AqLP9fZSKM8jdFg2WGhHQi1QbE54Wml5aDNyaUVDRGc&output=csv&gid=4',
    'Georgia': 'https://docs.google.com/spreadsheet/ccc?key=0AqLP9fZSKM8jdFg2WGhHQi1QbE54Wml5aDNyaUVDRGc&output=csv&gid=1'
}

name_key = "English Name"
group_key = "Group"

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

def load_samples(cache=True):
    samples = {}
    for name in resources:
        data = get_data(name, cache=cache)
        for line in data:
            header = line[name_key]
            concept = line[group_key] or '?'
            samples.setdefault(concept, []).append( header )
    return samples
