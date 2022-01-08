import json

from itertools import chain

from datapoint import datarange, bp


def getdata_from_file(file_path):
    """Retrieve json data from a file by filepath"""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def dump(data, file_path):
    """Save json data to a file by filepath"""
    with open(file_path, 'w+') as file:
        json.dump(data, file, indent='  ')

def build_chain(start1, stop1, start2, stop2):
    """Generate list of 2 chained ranges"""
    return chain(range(start1, stop1+1), range(start2, stop2+1))

def build_data(chain_):
    """Bulds data of a list in required form"""
    return [{'id':i, 'name': f'Test {i}'} for i in chain_]


def retrieve_data(id):
    if id == 3:
        # 3 source was not described in task. Supposed to be a simple python object
        data = build_data(build_chain(*datarange[id]))
    elif id in (1, 2):
        # 1 & 2 sources are json files

        # Next 2 lines used for json generation
        # data = build_data(build_chain(*datarange[id]))
        # dump(data, f'datapoint/data/data{id}.json')

        data = getdata_from_file(f'{bp.root_path}/data/data{id}.json')
    else:
        raise Exception(f"Data {id=} is not in allowed (1, 2, 3)")

    return data


def retrieve_data_safe(id):
    """Task requires any errors of retrieving data should be considered as empty data"""
    data = []
    try:
        data = retrieve_data(id)
    except Exception as e:
        pass
    finally:
        return data


def retrieve_data_thread(id, results):
    """Get data and put to results inside Threads"""
    results.append(retrieve_data(id))


def mergesort_lists(*lists):
    """Supposet that lists are sorted

    Complexity is O(n+m+l+...)
    """
    def next_(iterator):
        """ Provide dict {"id":id , ...} for id comparison"""
        return next(iterator, {'id': float("inf")})

    iters = []  # List iterators are stored here
    items = []  # Dictionaries with id and other stuff are stored here
    values = [] # id's are stored here for comparison
    for l in lists:
        i = iter(l)
        iters.append(i)

        it = next_(i)
        items.append(it)

        v = it['id']
        values.append(v)
    
    # To build merged list
    merged = []

    while True:
        min_ = float('inf')  # define current min as infinity
        pos = -1
        # Traverse to find a min value to apend it next
        for idx, val in enumerate(values):
            if val < min_:
                min_ = val
                pos = idx

        # if min value was not reached then all are inf and that means StopIteration for all lists
        if pos == -1:
            return merged

        merged.append(items[pos])

        # Change iterators and binded data
        iterator = iters[pos]
        item = next_(iterator)
        value = item['id']

        items[pos] = item
        values[pos] = value
