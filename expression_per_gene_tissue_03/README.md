Expression_per_gene_tissue_03: Generic
======================================

An example of how to configure a simple generic API under ADAMA. One passes a GET requesting a specific "locus" to the $API/$NS/$SERVICE_$VERSION/search endpoint. The result is fetched and returned. This example demonstrates excellent manual error handling and parameter validation.

Action: Test locally (assuming you've checked out this repo)
```
cd expression_per_gene_tissue_03
python
>> import main
>> main.search({'transcript':'AT1G33930.1', 'format':'json', 'material':'Young'})
('application/json; charset=ISO-8859-1', '{"expression":[{"elem_tissue":"YOUNG","elem_conc":"1.80e-05","elem_ratio":"0.0048","elem_conc2":"1.37e-05","elem_ratio2":"0.00015","elem_cycle_time":"29.41","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.33"}]}\n')
```

Action: Enroll via Gitrepo
```
curl -sk -L -X POST $API/$NS/services -F "git_repository=https://github.com/mwvaughn/jcvi-rtpcr-demos.git" -F "metadata=expression_per_gene_tissue_03" -H "Authorization: Bearer $TOKEN"

{
    "message": "registration started", 
    "result": {
        "list_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.2/list", 
        "notification": "", 
        "search_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.2/search", 
        "state_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.2"
    }, 
    "status": "success"
}
```
Result: Successful enrollment

Action: Check status
```
curl -sk -L -X GET "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.2"

{
    "result": {
        "service": {
            "code_dir": "/tmp/tmpCqvsMV/user_code", 
            "description": "JCVI RTPCR Webservice Generic", 
            "json_path": "", 
            "language": "python", 
            "main_module": "expression_per_gene_tissue_03/main.py", 
            "metadata": "expression_per_gene_tissue_03", 
            "name": "expression_per_gene_tissue_03", 
            "namespace": "vaughn-dev", 
            "notify": "", 
            "requirements": [], 
            "type": "generic", 
            "url": "http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue", 
            "version": 0.2, 
            "whitelist": [
                "129.114.97.2", 
                "bar.utoronto.ca", 
                "www.jcvi.org", 
                "129.114.97.1", 
                "129.116.84.203"
            ], 
            "workers": [
                "cd44348c6da61456110c19775bd569db6f83736e7182c26797037b531550fb0e"
            ]
        }
    }, 
    "status": "success"
}
```
Result: Seems to have worked

Action: Test it out via curl
```
curl -sk -L -X GET "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.2/search?transcript=AT1G33930.1&format=json&material=Young"

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
