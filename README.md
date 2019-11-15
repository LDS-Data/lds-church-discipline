## Introduction
The LDS Church Discipline Database is an effort to promote understanding of LDS church disciplinary practices by compiling all publicly documented instances of formal discipline by The Church of Jesus Christ of Latter-day Saints as well as its predecessors, the Church of Christ and the Church of Jesus Christ of Latter Day Saints (no hyphen).

**This database is neither affiliated with nor endorsed by The Church of Jesus Christ of Latter-day Saints (also known as the LDS Church or Mormon Church). The title "LDS Church Discipline Database" is meant to accurately reflect the contents and focus of the database, but does not in any way imply that The Church of Jesus Christ of Latter-day Saints approves of or is in any way responsible for the contents of the database.**

## Call for Contributions
This database is far from complete. We're calling for any _publicly documented_ instances of formal church discipline not represented here, especially:
* acquittals / "no action" results
* positive interactions with church discipline
* unusual penalties or outcomes (e.g. revocation of authority to exercise the priesthood)

_Please send additions and corrections to [ldschurchdata@gmail.com](mailto:ldschurchdata@gmail.com) or make edits directly in GitHub. See [Contributing](#contributing) for more information._

## The Database

Strictly speaking the database is contained in [discipline.json](https://github.com/LDS-Data/lds-church-discipline/blob/master/discipline.json) and [discipline.tsv](https://github.com/LDS-Data/lds-church-discipline/blob/master/discipline.tsv), but we also present it for your perusal here:

{% include_relative discipline.md %}

## Sources Consulted
* Wikipedia Category: [People excommunicated by The Church of Jesus Christ of Latter-day Saints](https://en.wikipedia.org/wiki/Category:People_excommunicated_by_The_Church_of_Jesus_Christ_of_Latter-day_Saints)
* Wikipedia Category: [People excommunicated by the Church of Christ (Latter Day Saints)](https://en.wikipedia.org/wiki/Category:People_excommunicated_by_the_Church_of_Christ_(Latter_Day_Saints))
* Wikipedia: [List of former or dissident LDS](https://en.wikipedia.org/wiki/List_of_former_or_dissident_LDS)
* [26 Apr 1839 Far West council minutes](http://emp.byui.edu/satterfieldb/rel341/Mission%20to%20England%20Meeting%20April%2026.html)
* [Sarah Pratt: The Shaping of an Apostate](https://archive.org/details/SarahPrattShapingOfAnApostate) by Richard S. Van Wagoner.

## Contributing

The scope of this project is too large for one human being to accomplish in a reasonable amount of time. I am hoping to do what I can and also to lay a groundwork for others to build on.

The [Inbox](#inbox) lists individuals who need to be investigated and documented. That's a great place to start.

[Sources To Consult](#sources-to-consult) lists sources that are known to contain records of church disciplinary action, but which need to be combed through for specific individuals, which could go to the Inbox.

If you know of additional individuals please add them to the [Inbox](#inbox).

If you know of additional sources please add them to [Sources To Consult](#sources-to-consult).

When you have a contribution to make, here's how to get it into the database:

### Email
Tips, additions, corrections, or any other feedback are welcome at [ldschurchdata@gmail.com](mailto:ldschurchdata@gmail.com). This is the route to take if you wish to remain anonymous.

### Contributing Directly on GitHub

The database is hosted on the GitHub code sharing site. This makes it easy for contributors to directly edit the files involved, as follows:

1. Click "View on GitHub" above
2. If you have a GitHub account, log in; otherwise, create a new account and log in.
3. Open the file within the project that you wish to edit by clicking on its filename. For example, this file is [README.md](https://github.com/LDS-Data/lds-church-discipline/blob/master/README.md), and the main data file is [discipline_base.json](https://github.com/LDS-Data/lds-church-discipline/blob/master/discipline_base.json).
4. When the file opens in your browser, click the pencil icon to edit the file.
5. Make the desired changes, then add a description of the changes and click "Propose file change". This will make your changes available for me to review and (if accepted) incorporate into the database.

## Format
The database is stored in JSON format in [discipline_base.json](https://github.com/LDS-Data/lds-church-discipline/blob/master/discipline_base.json). The build script `scripts/build.sh` transforms this into an expanded form, [discipline.json](https://github.com/LDS-Data/lds-church-discipline/blob/master/discipline.json) as well as [discipline.tsv](https://github.com/LDS-Data/lds-church-discipline/blob/master/discipline.tsv) and the Markdown document [discipline.md](https://github.com/LDS-Data/lds-church-discipline/blob/master/discipline.md).

An entry in `discipline_base.json` looks like this:

```json
  {
    "name": "Jesse Gause",
    "wikipedia_url": "https://en.wikipedia.org/wiki/Jesse_Gause",
    "jsp_url": "https://www.josephsmithpapers.org/person/jesse-gause",
    "birth_date": "1785",
    "death_date": "1836?",
    "sections": [
      "19th Century"
    ],
    "date_md": "prob. 3 Dec 1832",
    "tagline_md": "First Presidency member and missionary",
    "notes_md": "[Apparently excommunicated](https://www.josephsmithpapers.org/person/jesse-gause), for reasons unknown. A former Quaker and Shaker, his conversion to Mormonism introduced strain on his marriage that may have been a factor in his estrangement from the church.",
    "outcome": "excommunicated"
  }
```

`name`, `date_md`, and `outcome` are required. Other fields should be included if possible, but can be omitted. The fields are documented in more detail [here](docs/fields.md).

Fields ending with `_md` are in the Markdown format. That allows links and italics and other formatting to be included. We're using Github-flavored markdown. You can learn more about it [here](https://guides.github.com/features/mastering-markdown/).

Entries _must_ link to primary or secondary resources documenting all factual claims in the entry. It is acceptable to rely on Wikipedia if the Wikipedia article itself seems to justify its claims well; otherwise, you need to dig deeper to find more trustworthy sources.


## Inbox

The following are believed to have undergone formal church discipline but this needs to be investigated and documented:

* Frederick G. Williams
* Art Bulla
* Marisa and Carson Calderwood
* Frank J. Cannon
* John Q. Cannon
* Albert Carrington
* Benjamin L. Clapp
* Alpheus Cutler
* Ed Decker
* Steven Fales
* Antonio A. Feliz
* John Fitzgerald—1973
* John E. Forsgren
* Walter M. Gibson
* Matthew P. Gill
* William S. Godbe
* Gudmund Gudmundson
* Isaac C. Haight
* James D. Harmston
* Elias L. T. Harrison
* Glenn Helzer
* Leroy S. Johnson
* Charles W. Kingston
* John Hyrum Koyle
* Alma Dayer LeBaron Sr.
* Joel LeBaron
* Verlan M. LeBaron
* John D. Lee
* Amasa Lyman
* Amy and Jake Malouf
* Leonard Matlovich
* William McCary
* Richard Miller (agent)
* Brian David Mitchell
* Joseph Morris (Latter Day Saints)
* Joseph White Musser
* John E. Page
* W. W. Phelps 1847 excommunication (#3)
* Sidney Rigdon
* William Smith
* Third Convention
* Edward Tullidge
* Douglas A. Wallace—1976
* Lyman Wight
* Anne Wilde
* John W. Woolley
* Lorin C. Woolley
* "a bunch of the people who were early mormon fundamentalists and after the second manifesto"
* "the recent men convicted of child sexual abuse who were bishops or church leaders or part of scandals"

## Revision Needed
Entries which (potentially) are not up to current standards:

* Byron Merchant
* Sonia Johnson
* David Wright
* Brent Metcalfe
* Janice Merrill Allred
* Margaret Toscano
* Shane Whelan
* Rhonda Whelan
* Kate Kelly
* John Dehlin
* Bruce Holt
* Jeremy Runnells
* Sam Young
* Bill Reel
* Leah and Cody Young
* James Strang (wordsmithing needed)

## Sources To Consult
Sources from which church discipline actions should be gleaned:

* History of the Church
* Kirtland High Council Minutes
* [Order of Aaron thesis](https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=5669&context=etd)
* 1940s _Improvement Era_ excommunication notices
* _Modern Polygamy and Mormon Fundamentalism: The Generations after the Manifesto_ by Brian Hales

When a source has been fully combed through, move it to [Sources Consulted](#sources-consulted).

## Unconfirmed

Individuals for whom church discipline has been claimed but for which sufficient evidence has not been found.

* Martha Nibley Beck——Scholar and author—Excommunicated??? for her public writings which were deemed to be critical of the church. She was a part time faculty at BYU at the time and is the daughter of Hugh Nibley, a well-known Mormon apologist.

* Jason Derek Brown, 489th fugitive to be placed on the FBI Ten Most Wanted list. No evidence of excommunication yet found.

* [Charles A. Foster](https://en.wikipedia.org/wiki/Charles_A._Foster_(Latter_Day_Saints)) (1815-1904)——_Navuoo Expositor_ publisher—Excommunicated???

* [Hiram Page](https://en.wikipedia.org/wiki/Hiram_Page)—Wikipedia categorizes him as having been excommunicated, but I find no evidence of this. [A 1987 thesis](https://scholarsarchive.byu.edu/etd/5142/) states explicitly that there is no evidence of excommunication or withdrawal of his license (p. 57)

* [Jacob Whitmer](https://en.wikipedia.org/wiki/Jacob_Whitmer) (2 Feb 1800-21 Apr 1856)——One of the Eight Witnesses of the Book of Mormon—Joseph Smith Papers says he was [disaffected from the church in 1838](https://www.josephsmithpapers.org/person/jacob-whitmer), but I find no record of disciplinary action. [A Feb 1989 Ensign article](https://web.archive.org/web/20191113003645/http://www.churchofjesuschrist.org/study/ensign/1989/02/true-to-the-book-of-mormon-the-whitmers?lang=eng) explicitly states that he was never tried for his church membership. The Encyclopedia of Mormonism simply [states that he became "inactive"](https://eom.byu.edu/index.php/Book_of_Mormon_Witnesses). Wikipedia is likely wrong to have categorized him as excommunicated.

* [Mary Mussleman Whitmer](https://en.wikipedia.org/wiki/Mary_Mussleman_Whitmer) (27 Aug 1778-Jan 1856)——Book of Mormon witness, early Mormon matriarch—She said that, in the time when the Book of Mormon was being translated, a heavenly messenger named Brother Nephi [showed her that golden plates](https://web.archive.org/web/20191113083221/https://journal.interpreterfoundation.org/another-account-of-mary-whitmers-viewing-of-the-golden-plates/) as she went out to milk the cows. I have not been able to find evidence she underwent church discipline, other than claims that the entire Whitmer family was excommunicated. Wikipedia may have her wrongly categorized as excommunicated.

* [Peter Whitmer Sr.](https://en.wikipedia.org/wiki/Peter_Whitmer_Sr.) (14 Apr 1773-12 Aug 1854)——Early Mormon patriarch—With Mary Musselman Whitmer, the father of the Whitmer family influential in early Mormonism. [He became disaffected from the church in 1838](https://www.josephsmithpapers.org/person/peter-whitmer-sr) but I find no evidence he underwent church discipline, except that many articles claim the entire Whitmer family was excommunicated, and Wikipedia categorizes him as excommunicated.
