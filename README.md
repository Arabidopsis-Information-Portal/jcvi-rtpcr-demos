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
    * Example URL constructed by the demo: http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue?gene=AT1G33930.1&format=json&Submit=Search

This exposes the first of several planned web service end points.
* Expression levels per gene per tissue (done).
* Genes for which expression in tissue A exceeds that in tissue B.
* Metadata about images for a given plant ontology term (including image IDs).
* Metadata about images for a given gene (including image IDs).
* Image given an image ID.

Not done: proper handling of error conditions.

Example Source Data
-------------------
```
{"expression":[
    {"elem_tissue":"FLOWER",
     "elem_conc":"0.00030",
     "elem_ratio":"0.062",
     "elem_conc2":"0.00017",
     "elem_ratio2":"0.0021",
     "elem_cycle_time":"25.82",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"0.081"},
    {"elem_tissue":"IAA",
     "elem_conc":"0.14",
     "elem_ratio":"0.036",
     "elem_conc2":"0.092",
     "elem_ratio2":"0.0012",
     "elem_cycle_time":"25.35",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"0.34"},
    {"elem_tissue":"LEAF",
     "elem_conc":"0.057",
     "elem_ratio":"0.040",
     "elem_conc2":"0.035",
     "elem_ratio2":"0.0015",
     "elem_cycle_time":"26.81",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"0.44"},
    {"elem_tissue":"NACL",
     "elem_conc":"9.19e-05",
     "elem_ratio":"0.047",
     "elem_conc2":"4.25e-05",
     "elem_ratio2":"0.0015",
     "elem_cycle_time":"25.37",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"0.63"},
    {"elem_tissue":"ROOT",
     "elem_conc":"0.00089",
     "elem_ratio":"0.00039",
     "elem_conc2":"0.00031",
     "elem_ratio2":"6.29e-06",
     "elem_cycle_time":"33.43",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"0.59"},
    {"elem_tissue":"SALICYLIC",
     "elem_conc":"7.32e-05",
     "elem_ratio":"0.012",
     "elem_conc2":"9.86e-05",
     "elem_ratio2":"0.00085",
     "elem_cycle_time":"26.62",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"1.23"},
    {"elem_tissue":"YOUNG",
     "elem_conc":"1.80e-05",
     "elem_ratio":"0.0048",
     "elem_conc2":"1.37e-05",
     "elem_ratio2":"0.00015",
     "elem_cycle_time":"29.41",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"0.33"}]}
```
