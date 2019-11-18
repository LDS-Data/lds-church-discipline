SEP='—'

def lifespan(obj):
    if 'birth_date' in obj:
        if 'death_date' in obj:
            return " (%s-%s)" % (obj['birth_date'], obj['death_date'])
        else:
            return " (b. %s)" % obj['birth_date']
    else:
        if 'death_date' in obj:
            return " (d. %s)" % obj['death_date']
        else:
            return ""

def name_maybe_with_link(obj):
    try:
        return "[%s](%s)" % (obj['name'], obj['wikipedia_url'])
    except KeyError:
        return obj['name']

def name_and_lifespan(obj):
    return "".join([name_maybe_with_link(obj), lifespan(obj)])

if __name__=="__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Expand JSON by processing various fields.')
    parser.add_argument("filename", help="Path to JSON to expand")

    args = parser.parse_args()

    with open(args.filename) as r:
        data = json.load(r)

    current_sections = None
    for obj in data:

        if obj['sections'] != current_sections:
            print("%s %s" % ('#'*(2+len(obj['sections'])), obj['sections'][-1]))

        current_sections = obj['sections']

        print("* %s" % SEP.join([name_and_lifespan(obj), obj['date_md'], obj.get('tagline_md', ""), obj['notes_md']]))
        print()
