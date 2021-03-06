import json
import sys

from expand_json import markdown_to_txt


mapping = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

def int_if_possible(x):
    try:
        return int(x)
    except ValueError:
        sys.stderr.write("Not an integer: %s\n" % x)
        return 999999999

def obj_to_date(obj):
    return markdown_to_txt(obj['date'])

def obj_to_key(obj):
    date = obj_to_date(obj).replace('?','')

    parts = date.split()

    parts = [x for x in map(lambda y: int_if_possible(mapping.get(y, y)), parts)]

    return [x for x in reversed(parts)]

if __name__=="__main__":

    import shutil

    # Make a backup
    shutil.copyfile("discipline_base.json", "discipline_base.json.bak")

    with open("discipline_base.json") as r:
        data = json.load(r)

    dated_data =  list(filter(lambda obj: 'sections' not in obj or 'Uncertain Date' not in obj['sections'], data))
    undated_data = list(filter(lambda obj: 'sections' in obj and 'Uncertain Date'     in obj['sections'], data))

    resorted = [x for x in sorted(dated_data, key=obj_to_key)]

    resorted.extend(undated_data)

    with open("discipline_base.json", "w") as w:
        json.dump(resorted, w, indent=2, ensure_ascii=False)
