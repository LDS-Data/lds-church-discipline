# Data Fields

## type Discipline

* name: The name by which the person is typically known
* wikipedia_url: the URL of the Wikipedia article specific to the person, if any
* jsp_url: the URL of the Joseph Smith Papers biography, if any
* birth_date: the textual representation of the person's date of birth, if known
* birth_date_md: the Markdown represenation of the person's date of birth, if known
* death_date: the textual representation of the person's date of death, if known
* death_date_md: the Markdown representation of the person's date of death, if known
* sections: the groupings or headings to which this entry belongs, broadest first. For example: ["19th Century", "The Followers of Isaac Russell"]
* date: the plain text representation of the date on which this disciplinary action took place.
* date_md: the Markdown representation of the date on which this disciplinary action took place.
* for: the formal reasons given for the disciplinary action (if any), e.g. "apostasy", "teaching false doctrine", "committing a hijacking", etc. Either a string or an array of strings.
* alt_for: unofficial reasons for the disciplinary action. Either a string or an array of strings.
* tagline: the plaintext representation of the tagline which attempts to succinctly summarize the person and their contribution
* tagline_md: the Markdown representation of the tagline which attempts to succinctly summarize the person and their contribution
* notes: the plaintext representation of the notes
* notes_md: the Markdown representation of the notes
* office: the priesthood office at time of disciplinary action, if known
* outcome: the outcome of the disciplinary action. The primary options are:
  * excommunicated: also referred to as being "cut off" from the church, or simply no longer being considered a member (not at the member's request).
  * excommunicated-at-own-request: this primarily occurred before the 1989 handbook revision which permitted resignation, [probably triggered by a lawsuit by Norman Hancock](https://web.archive.org/web/20190907202136/http://mormon-alliance.org/casereports/volume3/part1/v3p1c05.htm). (Excommunication was previously the only route out of church membership.)
  * disfellowshipped: various privileges of membership were suspended but membership was retained.
  * resigned: a member requested to no longer be a member (not by excommunication) while not under immediate threat of church discipline.
  * resigned-in-response-to-discipline: a member resigned while under immediate threat of church discipline. Either a summons was received, or a council was in progress, or disciplinary action had been materially threatened.
  * priesthood-deathorized: the (male) member's priesthood authority was revoked. This may only have happened to Matthias F. Cowley.
  * no-action: a council was held but no action was taken
  * council-averted: a council was planned and a summons delivered to the member, but was not ultimately held. In this case the "date" represents the date the council had been planned for.
  These same options can be have a following question mark to indicate uncertainty about the outcome.
* sex: "male" or "female" (we can add other options if we come across them)
* tags: an array of plaintext strings marking distinguishing features of this entry. Examples include sources ("improvement-era") to help separate particular groups of entries.
* location: the plaintext representation of the location at which the disciplinary action was carried out, if known
* location_md: the Markdown representation of the location at which the disciplinary action was carried out, if known
* unit: the plaintext representation of the church unit in which the discipline was carried out, if known
* unit_md: the Markdown representation of the church unit in which the discipline was carried out, if known

### Derived

* best_date: the text representation of the best estimate for the date on which this disciplinary action took place. If date_txt is "abt. 1888" then this would be "1888". If date_txt is "abt. 3 Jul 1919" then this would be "3 Jul 1919".
* best_year: the best estimate of the year
* best_month: the best estimate of the month, if known
* best_day: the best estimate of the day of month, if known
* best_birth_date: the text representation of the best estimate for the date on which the person was born, if known
* best_birth_year: the best estimate of the year the person was born, if known
* best_birth_month: the best estimate of the month the person was born, if known
* best_birth_day: the best estimate of the day of month the person was born, if known
* best_death_date: the text representation of the best estimate for the date on which the person died, if known
* best_death_year: the best estimate of the year the person died, if known
* best_death_month: the best estimate of the month the person died, if known
* best_death_day: the best estimate of the day of month the person died, if known
* country
* adm1
* adm2
* adm3
* adm4
* best_location
* best_country
* best_adm1
* best_adm2
* best_adm3
* best_adm4
* friendly_location: a more natural form of the location

### Sporadically Used

* baptism_date: the text representation of the date of the person's first baptism into the church (since they last were not in the church).
* birth_place: where the person was born. Sometimes we know this, might as well keep track of it.
* rebaptism_date: the text representation of the date of the person's next baptism after being excommunicated in this action (if applicable)
* recording_url: URL of a recording of the disciplinary council itself


### Contemplated

* marital_status: "married", "single", "divorced", "widowed"

* spouse_count: the number of spouses the person had at the time of the disciplinary action, whether legal, plural, or otherwise.
