import csv
import os
import sys

class Node(object):
    __slots__ = ['id', 'parent', 'children', 'text', 'bag_of_words']

    def __init__(self, id, text, parent='', children=[], bag_of_words=set()):
        self.id = id
        self.text = text
        self.parent = parent
        self.children = children
        self.bag_of_words = bag_of_words

    def __str__(self):
        return "id: %s\ntext: '%s'\nparent: '%s'\nchildren:%s\n" % (self.id, self.text,
                                                                    self.parent,
                                                                    self.children)

def root_level_builder(filename):
    data = {}
    records = []
    #TODO: cmdline args filename
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #skip code name rows
        print reader.next();
        for row in reader:
            #TODO: hardcode code/EN colums 0,6 allow user so specify
            records.append(Node(row[0], row[6]))

    print "%d codes added" % (len(records))

    #assumes CODE has same length()
    cur_len = 2
    max_len = len(records[0].id)
    #root nodes are first two digits
    while(cur_len < max_len):
        #find children
        while len(records) > 0:
            cur_rec = records.pop()
            pos_children = [rec for rec in records if cur_rec.id[0:cur_len] == rec.id[0:cur_len]]
            #sort pos_children
            pos_children.sort(key=lambda x: x.id, reverse=True)
            #update records removing current matches
            records[:] = [rec for rec in records if not cur_rec.id[0:cur_len] == rec.id[0:cur_len]]
            #get the root 
            cur_rec = pos_children.pop()
            #set the children as everyone else
            cur_rec.children = pos_children
            data.update({cur_rec.id : cur_rec})
        cur_len += 1
    print "%d root cats" % len(data)

    for key in data.keys():
        for child in data[key].children:
            data[key].bag_of_words.update([word.lower() for word in child.text.split(' ')])

if __name__  == "__main__":
    root_level_builder(sys.argv[1])
