from resort import obj_to_key

person_fields = set([
    'name',
    'sex',
    'office',
    'birth_date',
    'birth_place',
    'death_date',
    'wikipedia_url',
    'jsp_url',
    'tagline'
])

event_fields = set([
    'outcome',
    'notes',
    'date',
    'location',
    'unit',
    'for',
    'alt_for',
    'tags',
])

ignore_fields = set(['sections'])

if __name__=="__main__":
    import argparse
    import json
    from collections import defaultdict

    parser = argparse.ArgumentParser(description='Expand JSON by processing various fields.')
    parser.add_argument("filename", help="Path to JSON to expand")

    args = parser.parse_args()

    with open(args.filename) as r:
        data = json.load(r)

    people = defaultdict(dict)

    people_events = dict()

    for event in data:
        name = event['name']
        person = people[name]

        try:
            events = people_events[name]
        except KeyError:
            events = list()
            people_events[name] = events

        for field, value in list(event.items()):

            if field in person_fields or field.replace("_md","") in person_fields:
                try:
                    if person[field] == value:
                        event.pop(field)
                    else:
                        raise Exception("Person '%s' had %s=%s and %s=%s" % (event['name'], field, person[field], field, value))
                except KeyError:

                    person[field] = value
                    event.pop(field)

            elif field == 'baptism_date' or field == 'baptism_date_md' or field == 'rebaptism_date' or field == 'rebaptism_date_md':

                new_field = field.replace('rebaptism_','').replace('baptism_','')

                already_present = False

                try:
                    for b in person['baptisms']:

                        if b[new_field] == value:
                            already_present = True
                except KeyError:
                    person['baptisms'] = list()

                if not already_present:
                    b = dict()
                    b[new_field] = value
                    person['baptisms'].append(b)

            elif field in event_fields or field.replace("_md","") in event_fields:

                # event[field] = value
                pass

            elif field in ignore_fields or field.replace("_md","") in ignore_fields:
                event.pop(field)

            else:
                raise Exception("Unrecognized field '%s'" % field)

        events.append(event)

    for name, events in people_events.items():
        people[name]['events'] = events

    print(json.dumps(list(sorted(people.values(), key=lambda x: obj_to_key(x['events'][0])  )), indent=2, ensure_ascii=False))
