# Roadmap

Some directions to take things:

* Make JSON the "source of truth"? Right now the data is contained in README.md but this is messy. It might be better to make the JSON data primary. Either that or really embrace this "em-dash separated values" format?
* Better define the scope of the project. Are we including people who simply resigned? Do we only include notable figures, or everybody? Are all sorts of reasons included?
* Give a description of the various data fields
* Normalize the data? Name/lifespan/tagline are all duplicated across entries. Either that or use a script to enforce that there should be no variation in these.
* Add sex
* Add location
* Add baptism date
* Add rebaptism date, or indicate if it's known they never rejoined
* Separate formal charges from other notes
* Add a license
* Split the readme up into some separate files since it's so large
* Make Wikipedia URL and JSP URL their own fields
* Encode social networks? E.g. { "relationships": {"spouse": "Elizabeth Schott", "sibling": "John Whitmer", "mother": "Mary Musselman", "father": "Peter Whitmer, Sr."} }
* Replace lifespan years with specific dates if known
* Last but certainly not least, _expand coverage_!
