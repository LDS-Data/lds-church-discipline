
import re

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

md_to_txt = ("date", "tagline", "notes", "location", "unit")

if __name__=="__main__":
    import json

    with open('discipline_base.json') as r:
        data = json.load(r)

    data2 = list()

    for fields in data:
        for txt_field in md_to_txt:
            try:
                fields[txt_field] = markdown_to_txt(fields["%s_md" % txt_field])
            except KeyError:
                pass

        # fields['date_txt'] = markdown_to_txt(fields['date_md'])
        fields['best_date_txt'] = date_txt_to_best_date_txt(fields['date'])

        date_fields = date_rgx.match(fields['best_date_txt']).groupdict()
        fields['best_year'] = int(date_fields['year'])
        fields['best_month'] = date_fields['month']
        if date_fields['day'] is not None:
            fields['best_day'] = int(date_fields['day'])
        else:
            fields['best_day'] = None

        # fields['tagline'] = markdown_to_txt(fields['tagline_md'])
        # fields['notes'] = markdown_to_txt(fields['notes_md'])

        data2.append(fields)

    print(json.dumps(data, indent=2))
