Expression_per_gene_tissue_01: Query x AIP native response
==========================================================

An example of how to configure a simple query API under ADAMA. One passes a GET requesting a specific "transcript" to the $API/$NS/$SERVICE_$VERSION/search endpoint. The "material" term is optional and allows one to request data from a specific experiment. The result is fetched and returned as a prototypical AIP JSON document. In this specific case, the remote server is providing HTML that is being parsed and converted via specific code into a compliant data record. 

Action: Enroll via Gitrepo
```
curl -sk -L -X POST $API/$NS/services -F "git_repository=https://github.com/mwvaughn/jcvi-rtpcr-demos.git" -F "metadata=expression_per_gene_tissue_01" -H "Authorization: Bearer $TOKEN"
```

Action: Test service
```
curl -sk -L -X GET "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_01_v0.1/search?transcript=AT1G33930.1&material=Young"

{"result": [
{"expression_record": [{"cycle_time": "29.41", "absolute_concentration_stdev": "1.37e-05", "ratio_to_invariants_stdev": "0.00015", "cycle_time_stdev": "0.33", "material_text_description": "Young Siliques", "ratio_to_invariants": "0.0048", "absolute_concentration": "1.80e-05"}], "transcript": "AT1G33930.1", "class": "transcript_property", "source_text_description": "RT-PCR"}
],
"metadata": {"time_in_main": 0.5452890396118164},
"status": "success"}
```
