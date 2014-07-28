import unicodecsv


class Node(object):

    def __init__(self, _id, data):
        self.parent = ""
        self.id = _id
        self.data = data
        self.text = data[6]

    def append(self, children):
        self.children.append(children)


def _build_tree(nodes, depth):
    # TODO make me faster and smarter
    # add depth
    # runs ~4 mins on a core duo:/
    # currently it builds a flat list and set the parent id
    # node 0031 - parent 003
    # node 0032 - parent 003
    # node 00323 - parent 0032
    for n in nodes:
        for te in nodes:
            if n.id == te.id:
                continue
            wid = ""
            for j in te.id:
                wid += j
                if n.id.startswith(wid):
                    n.parent = wid


if __name__ == '__main__':
    nodes = []
    csv_file = open('data/cpv_2008_ver_2013.csv')
    # remove headers
    cfile = unicodecsv.reader(csv_file, encoding='utf-8')
    next(cfile)

    for i in cfile:
        i[0] = i[0].replace('-', '')
        n = Node(i[0], data=i)
        nodes.append(n)

    _build_tree(nodes, 2)
    # print the nodes with its parent id
    print [x.parent for x in nodes]
