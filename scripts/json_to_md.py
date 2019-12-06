import sys

from fields import ALT_FOR, DATE_MD, FOR, FRIENDLY_LOCATION, JSP_URL, NOTES_MD, OUTCOME, OUTCOME_MD, PLUS_NOTES_MD, RECORDING_URL, TAGLINE_MD, UNIT, UNIT_MD

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

def _conjunction(items):
    if type(items) == str:
        return items

    if len(items) == 1:
        return items[0]

    if len(items) == 2:
        return ' and '.join(items)

    return '%s and %s' % (', '.join(items[:-1]), items[-1])

def _capitalize_first_alpha(s):
    found = False

    a = list()

    for c in s:
        if c.isalpha() and not found:
            c = c.upper()
            found = True

        a.append(c)

    return ''.join(a)

def auto_notes_md(obj):
    s = _capitalize_first_alpha( obj[OUTCOME_MD] )
    try:
        s += ' in %s' % obj[FRIENDLY_LOCATION]
    except KeyError:
        pass

    try:
        s += ' by the %s' % obj[UNIT_MD]
    except KeyError:
        pass

    try:
        s += ' for %s' % _conjunction(obj[FOR])
    except KeyError:
        pass

    s += '.'

    return s

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
                pass

        parts = [name_and_lifespan(obj)]

        try:
            parts.append(obj[DATE_MD])
        except KeyError:
            sys.stderr.write("No '%s' for %s\n" % (DATE_MD, obj['name']) )

        try:
            parts.append(obj[TAGLINE_MD])
        except KeyError:
            pass

        try:
            notes_md = obj[NOTES_MD]
        except KeyError:
            notes_md = auto_notes_md(obj)

        try:
            notes_md += ' %s' % obj.pop(PLUS_NOTES_MD)
        except KeyError:
            pass

        parts.append(notes_md)


        print("* %s" % SEP.join(parts))
        try:
            print("  - Location: %s" % obj[FRIENDLY_LOCATION])
        except KeyError:
            pass

        try:
            print("  - Church unit: %s" % obj[UNIT])
        except KeyError:
            pass

        try:
            print("  - [Joseph Smith Papers biography](%s)" % obj[JSP_URL])
        except KeyError:
            pass

        try:
            print("  - [Recording](%s)" % obj[RECORDING_URL])
        except KeyError:
            pass

        print()
