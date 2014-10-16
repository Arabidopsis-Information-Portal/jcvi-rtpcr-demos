Web services for "Expression Profiling of the Arabidopsis Transcriptome"
========================================================================

Objective: Creating web services from JCVI's qPCR and promoter-reported work, which was a 2010 project. This will serve as a demo of how to perpetuate these (2010 project data in general) results which are useful to a few people but almost invisible. Site: http://www.jcvi.org/arabidopsis/qpcr/index.shtml

Service 1: ExpressionPerGenePerTissue
-------------------------------------

Service 2-inf: TBD
------------------

Notes from https://jira.araport.org/browse/DATA-84
--------------------------------------------------

...public URLs on prod.
* The old home page: http://www.jcvi.org/arabidopsis/qpcr/index.shtml
* The old form for getting a table of expression values per gene: http://www.jcvi.org/arabidopsis/qpcr/search.php
* The new web service demo: http://www.jcvi.org/arabidopsis/qpcr/MinimalForm_ExpressionPerGenePerTissue.html
    * Example URL constructed by the demo: http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue?gene=AT1G33930.1&format=html&Submit=Search

This exposes the first of several planned web service end points.
* Expression levels per gene per tissue (done).
* Genes for which expression in tissue A exceeds that in tissue B.
* Metadata about images for a given plant ontology term (including image IDs).
* Metadata about images for a given gene (including image IDs).
* Image given an image ID.

Not done: proper handling of error conditions.