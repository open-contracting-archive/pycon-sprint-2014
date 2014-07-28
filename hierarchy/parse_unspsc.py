import subprocess
import json
import re


FILENAME = "data/UNSPSC_English_v16_0901"
SEGMENT_RE = r"\A\s*(Segment)\s+(\d+)\s+([\w+|\s+]+)"
FAMILY_RE = r"\A\s*(Family)\s+(\d+)\s+([\w+|\s+]+)"
CLASS_RE = r"\A\s*(Class)\s+(\d+)\s+([\w+|\s+]+)"
ENTRIES_RE = r"\A\s*(\d+)\s+([\w+|\s+]+)(?=\s{2,})"


def main():
    # uncoment to test it on 10 pages
    ret = subprocess.call(['pdftotext', '-layout',  # '-f', '1', '-l', '10',
                           '%s.pdf' % FILENAME])
    if ret != 0:
        print "Error while processing file is 'pdftotext' missing?"
        return

    segments = {}

    with open('%s.txt' % FILENAME) as file:
        cur_seg = None
        cur_fam = None
        cur_cls = None
        for i in file.readlines():
            seg = re.match(SEGMENT_RE, i)
            fam = re.match(FAMILY_RE, i)
            cls = re.match(CLASS_RE, i)
            ent = re.match(ENTRIES_RE, i)
            if seg:
                segments[seg.groups()[1]] = {'title': seg.groups()[2],
                                             'families': {}}
                cur_seg = seg.groups()[1]
                cur_fam = None
                cur_cls = None
            elif fam:
                segments[cur_seg]['families'][
                    fam.groups()[1]] = {'title': fam.groups()[2],
                                        'classes': {}}
                cur_fam = fam.groups()[1]
            elif cls:
                segments[cur_seg]['families'][
                    cur_fam]['classes'][cls.groups()[1]] = {
                        'title': cls.groups()[2], 'entries': {}}
                cur_cls = cls.groups()[1]
            elif ent:
                segments[cur_seg]['families'][
                    cur_fam]['classes'][
                        cur_cls]['entries'][ent.groups()[0]] = {
                            'title': ent.groups()[1].strip(), 'desc': None}

    with open("data/unspsc.json", "w") as file:
        file.write(json.dumps(segments))

if __name__ == '__main__':
    main()
