# Data Fields

## type Discipline

* name: The name by which the person is typically known
* wikipedia_url: the URL of the Wikipedia article specific to the person, if any
* jsp_url: the URL of the Joseph Smith Papers biography, if any
* birth_date: the textual representation of the person's date of birth, if known
* death_date: the textual representation of the person's date of death, if known
* sections: the groupings or headings to which this entry belongs, broadest first. For example: ["19th Century", "The Followers of Isaac Russell"]
* date_md: the Markdown representation of the date on which this disciplinary action took place.
* date_txt: the plain text representation of the date on which this disciplinary action took place.
* best_date_txt: the text representation of the best estimate for the date on which this disciplinary action took place. If date_txt is "abt. 1888" then this would be "1888". If date_txt is "abt. 3 Jul 1919" then this would be "3 Jul 1919".
* best_year: the best estimate of the year
* best_month: the best estimate of the month, if known
* best_day: the best estimate of the day of month, if known
* tagline_md: the Markdown version of the tagline which attempts to succinctly summarize the person and their contribution
* tagline_txt: the plain text version of the tagline which attempts to succinctly summarize the person and their contribution
* notes_md: the Markdown version of the notes
* notes_txt: the plain text version of the notes
* outcome: the outcome of the disciplinary action. Usually either "excommunicated", "disfellowhipped", "resigned" or "no action". The main exception is Matthias Cowley's "priesthood deauthorization".

### Contemplated

* best_birth_date: the text representation of the best estimate for the date on which the person was born, if known
* best_birth_year: the best estimate of the year the person was born, if known
* best_birth_month: the best estimate of the month the person was born, if known
* best_birth_day: the best estimate of the day of month the person was born, if known
* best_death_date: the text representation of the best estimate for the date on which the person died, if known
* bets_death_year: the best estimate of the year the person died, if known
* best_death_month: the best estimate of the month the person died, if known
* best_death_day: the best estimate of the day of month the person died, if known
* location: the text representation of the location at which the disciplinary action was carried out, if known
* baptism_date: the text representation of the date of the person's first baptism into the church (since they last were not in the church).

* sex: "male" or "female" (we can add other options if we come across them)

* marital_status: "married", "single", "divorced", "widowed"

* spouse_count: the number of spouses the person had at the time of the disciplinary action, whether legal, plural, or otherwise.

* reasons: the formal reasons given for the disciplinary action (if any), e.g. "apostasy", "teaching false doctrine", "committing a hijacking", etc.