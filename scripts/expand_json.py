import re
import sys

import html2text
import mistune

md = mistune.Markdown()
html = html2text.HTML2Text()
html.ignore_links = True
def markdown_to_txt(markdown):
    return html.handle( md.render(markdown) ).strip().replace('\n',' ').replace('  ',' ')


date_rgx = re.compile("(?:(?P<day>\d?\d) )?(?:(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) )?(?P<year>\d\d\d\d)")

bet_rgx = re.compile("bet[.] (?P<year1>\d\d\d\d) and (?P<year2>\d\d\d\d)")
def date_txt_to_best_date_txt(date_txt):
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

def expand_date(date):
    fields = {
        'best_date_txt': date_txt_to_best_date_txt(date)
    }

    date_fields = date_rgx.match(fields['best_date_txt']).groupdict()
    fields['best_year'] = int(date_fields['year'])
    fields['best_month'] = date_fields['month']
    if date_fields['day'] is not None:
        fields['best_day'] = int(date_fields['day'])
    else:
        fields['best_day'] = None

    return fields

md_to_txt = ("date", "tagline", "notes", "location", "unit", "birth_date", "death_date")

if __name__=="__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Expand JSON by processing various fields.')
    parser.add_argument("filename", help="Path to JSON to expand")

    args = parser.parse_args()

    with open(args.filename) as r:
        data = json.load(r)

    sys.stderr.write("Expanding %s entries in %s\n" % (len(data), args.filename))

    data2 = list()

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

        for txt_field in md_to_txt:
            # plaintext -> Markdown, otherwise Markdown -> plaintext
            try:
                fields["%s_md" % txt_field] = fields[txt_field]
            except KeyError:
                try:
                    fields[txt_field] = markdown_to_txt(fields["%s_md" % txt_field])
                except KeyError:
                    pass

        try:
            fields.update(expand_date(fields['date']))
        except KeyError:
            sys.stderr.write("No date for %s\n" % fields['name'])

        data2.append(fields)

    print(json.dumps(data, indent=2, ensure_ascii=False))
