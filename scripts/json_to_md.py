import sys

SEP='—'

def lifespan(obj):
    if 'birth_date_md' in obj:
        if 'death_date_md' in obj:
            return " (%s-%s)" % (obj['birth_date_md'], obj['death_date_md'])
        else:
            return " (b. %s)" % obj['birth_date_md']
    else:
        if 'death_date_md' in obj:
            return " (d. %s)" % obj['death_date_md']
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
    parser.add_argument("--noheaders", help="Suppress output of section headers", action="store_true")

    args = parser.parse_args()

    with open(args.filename) as r:
        data = json.load(r)

    current_sections = None
    for obj in data:

        if not args.noheaders:
            try:
                if obj['sections'] != current_sections:
                    print("%s %s" % ('#'*(2+len(obj['sections'])), obj['sections'][-1]))
    
                current_sections = obj['sections']
            except KeyError:
                sys.stderr.write("No 'sections' for %s\n" % obj['name'])

        parts = [name_and_lifespan(obj)]

        try:
            parts.append(obj['date_md'])
        except KeyError:
            sys.stderr.write("No 'date_md' for %s\n" % obj['name'])

        try:
            parts.append(obj['tagline_md'])
        except KeyError:
            pass

        parts.append(obj['notes_md'])

        print("* %s" % SEP.join(parts))
        print()
