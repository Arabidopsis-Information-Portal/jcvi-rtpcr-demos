Web services for "Expression Profiling of the Arabidopsis Transcriptome"
========================================================================

Objective: Creating web services from JCVI's qPCR and promoter-reported work, which was a 2010 project. This will serve as a demo of how to perpetuate these (2010 project data in general) results which are useful to a few people but almost invisible. Site: http://www.jcvi.org/arabidopsis/qpcr/index.shtml

Service 1: ExpressionPerGenePerTissue
-------------------------------------
* expression_per_gene_tissue_01: Query; Transforms parameters; Returns AIP schema by scraping server HTML response
* expression_per_gene_tissue_02: Query; Transforms parameters; Returns AIP schema by transforming server JSON response
* expression_per_gene_tissue_03: Generic; Transforms parameters; Returns service native JSON or HTML
* expression_per_gene_tissue_04: Passthrough; Uses service native parameters; Returns service native response

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
    {"elem_tissue":"YOUNG",
     "elem_conc":"1.80e-05",
     "elem_ratio":"0.0048",
     "elem_conc2":"1.37e-05",
     "elem_ratio2":"0.00015",
     "elem_cycle_time":"29.41",
     "elem_target_id":"AT1G33930.1",
     "elem_cycle_time2":"0.33"}]}
```

Example AIP-schema response
---------------------------
```
{"result":[
    {"expression_record":[
        {"cycle_time":"29.41",
         "absolute_concentration_stdev":"1.37e-05",
         "ratio_to_invariants_stdev":"0.00015",
         "cycle_time_stdev":"0.33",
         "material_text_description":"Young Siliques",
         "ratio_to_invariants":"0.0048",
         "absolute_concentration":"1.80e-05"}],
     "transcript":"AT1G33930.1",
     "class":"transcript_property",
     "source_text_description":"RT-PCR"}],
 "metadata":
    {"time_in_main":0.5054709911346436},
 "status":"success"}
```
