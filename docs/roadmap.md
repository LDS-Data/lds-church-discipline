# Roadmap

Some directions to take things:

* Normalize the data? Name/lifespan/tagline are all duplicated across entries. Either that or use a script to enforce that there should be no variation in these.
* Split the readme up into some separate files since it's so large
* Encode social networks? E.g. { "relationships": {"spouse": "Elizabeth Schott", "sibling": "John Whitmer", "mother": "Mary Musselman", "father": "Peter Whitmer, Sr."} }
* Replace generated Markdown with Jekyll templating?
* Last but certainly not least, _expand coverage_!

## 0.9
* ~~Give a description of the various data fields~~
* ~~Make Wikipedia URL and JSP URL their own fields~~
* ~~Add sex~~
* ~~Add location~~
* ~~Make JSON the "source of truth"? Right now the data is contained in README.md but this is messy. It might be better to make the JSON data primary. Either that or really embrace this "em-dash separated values" format?~~
* ~~Autogenerate "Unconfirmed"~~
* Add a license
* Replace lifespan years with specific dates if known
* Better define the scope of the project. Are we including people who simply resigned? Do we only include notable figures, or everybody? Are all sorts of reasons included?
* Extract cleaned versions of all locations and dates

## 1.0

* Integrate the 1940s Improvement Eras
* Process the inbox until no more than five entries remain
* Add baptism date
* Add rebaptism date, or indicate if it's known they never rejoined
* Separate formal charges from other notes
* Review all taglines and notes to improve neutral point of view
