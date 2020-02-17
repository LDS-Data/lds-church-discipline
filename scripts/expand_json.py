import re
import sys

import html2text
import mistune

from fields import BIRTH_PLACE, OUTCOME, PLUS_NOTES

_md = mistune.Markdown()
_html = html2text.HTML2Text()
_html.ignore_links = True
def markdown_to_txt(markdown):
    return _html.handle( _md.render(markdown) ).strip().replace('\n',' ').replace('  ',' ')


date_rgx = re.compile("(?:(?P<day>\d?\d) )?(?:(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) )?(?P<year>\d\d\d\d)")

bet_rgx = re.compile("bet[.] (?P<year1>\d\d\d\d) and (?P<year2>\d\d\d\d)")
def date_txt_to_best_date_txt(date_txt):
    #sys.stderr.write(f"date_txt: {date_txt}\n")

    best = date_txt\
        .replace('?','')\
        .replace("prob. ","")\
        .replace('abt. ','')\
        .replace('by ','')\
        .replace("spring/summer", "21 Jun")\
        .replace("summer", "7 Aug")

    # print("best: %s" % best)

    m = bet_rgx.match(best)
    if m:
        year1 = int(m.groupdict()['year1'])
        year2 = int(m.groupdict()['year2'])
        return str(int(year1 + (year2-year1)/2))
        # return "2099"
    #
    # if best.startswith('bet. '):
    #     date1,date2 = [date_fields_to_date(x.groupdict()) for x in date_rgx.finditer(best[5:])]
    #     return date1 + (date2 - date1) / 2

    date_txt = next(date_rgx.finditer(best)).group()
    # print("date_txt: %s" %tdate_txt)
    return date_txt

def expand_date(date, prefix=""):

    fields = {
        'best_%sdate' % prefix: date_txt_to_best_date_txt(date)
    }

    date_fields = date_rgx.match(fields['best_%sdate' % prefix]).groupdict()
    fields['best_%syear' % prefix] = int(date_fields['year'])
    fields['best_%smonth' % prefix] = date_fields['month']
    if date_fields['day'] is not None:
        fields['best_%sday' % prefix] = int(date_fields['day'])
    else:
        fields['best_%sday' % prefix] = None

    return fields

regioned_countries = set(['United States'])
administrative_levels = ["country", "adm1", "adm2", "adm3", "adm4"]
def expand_location(location):
    fields = {
        'best_location': location.replace("?","")
    }

    parts = location.split(", ")
    parts.reverse()

    best_parts = fields['best_location'].split(", ")
    best_parts.reverse()
    for i, part in enumerate(parts):
        fields[administrative_levels[i]] = part
        fields['best_%s' % administrative_levels[i]] = best_parts[i]

    fields['friendly_location'] = friendly_location(fields['best_location'])

    return fields

def friendly_location(location):
    parts = location.split(", ")
    parts.reverse()

    ignore = set()

    if parts[0] == 'United States' and len(parts) > 1:
        ignore.add(0)

    if len(parts) >= 4:
        # Ignore the county / sub-region if it's there
        ignore.add(2)

    output_parts = list()
    for i, part in enumerate(parts):
        if part and part != '?' and i not in ignore:
            output_parts.append(part)

    output_parts.reverse()
    return ', '.join(output_parts)

# Autodetect Markdown or plaintext and put into base or _md suffixed entries accordingly
md_to_txt = ("date", "tagline", "notes", "location", "unit", "birth_date", "death_date", "baptism_date", "rebaptism_date", OUTCOME, BIRTH_PLACE, PLUS_NOTES)

if __name__=="__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Expand JSON by processing various fields.')
    parser.add_argument("filename", help="Path to JSON to expand")

    args = parser.parse_args()

    with open(args.filename) as r:
        data = json.load(r)

    sys.stderr.write("Expanding %s entries in %s\n" % (len(data), args.filename))

    for fields in data:

        try:
            if fields['tagline'] == "":
                sys.stderr.write("Empty 'tagline' for %s\n" % fields['name'])
        except KeyError:
            pass

        try:
            if fields['tagline_md'] == "":
                sys.stderr.write("Empty 'tagline_md' for %s\n" % fields['name'])
        except KeyError:
            pass

        for field in md_to_txt:
            try:
                raw = fields[field]

                txt = markdown_to_txt(raw)

                if txt == raw:
                    # The content was plaintext already so set the Markdown to the plaintext
                    md = txt
                else:
                    # The content was Markdown so treat it accordingly
                    md = raw

                fields[field] = txt
                fields['%s_md' % field] = md
            except KeyError:
                pass

        try:
            fields.update(expand_date(fields['date']))
        except KeyError:
            sys.stderr.write("No date for %s\n" % fields['name'])

        try:
            fields.update(expand_date(fields['birth_date'], prefix="birth_"))
        except KeyError:
            pass

        try:
            fields.update(expand_date(fields['death_date'], prefix='death_'))
        except KeyError:
            pass

        try:
            fields.update(expand_location(fields['location']))
        except KeyError:
            pass

    print(json.dumps(data, indent=2, ensure_ascii=False))
