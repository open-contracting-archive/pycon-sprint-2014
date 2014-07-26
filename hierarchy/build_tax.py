import csv
import os
import sys

class Node(object):
    __slots__ = ['id', 'parent', 'children', 'text']

    def __init__(self, id, text, parent='', children=[]):
        self.id = id
        self.text = text
        self.parent = parent
        self.children = children

    def __str__(self):
        "id: %s\n\
         text: '%s'\n\
         parent: '%s'\n\
         children:%s\n" % (self.id, self.text, self.parent, self.children)


def bottom_up_builder():
    data = {}
    records = []
    #TODO: cmdline args filename
    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        count = -1;
        #TODO: hardcode code/EN colums 0,6 allow user so specify
        for row in reader:
            count += 1;
            if count == 0:
                continue
            records.append({ row[0] : Node(row[0], row[6])})
        print "processed %d lines" % count

    print "%d codes added" % (len(records))






if __name__  == "__main__":
    bottom_up_builder()

