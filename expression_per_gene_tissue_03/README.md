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
        "list_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.1/list", 
        "notification": "", 
        "search_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.1/search", 
        "state_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.1"
    }, 
    "status": "success"
}
```
Result: Successful enrollment

Action: Check status
```
curl -sk -L -X GET "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.1"

{
    "result": {
        "service": {
            "code_dir": "/tmp/tmprTt9WO/user_code", 
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
            "version": 0.1, 
            "whitelist": [
                "129.114.97.2", 
                "www.jcvi.org", 
                "129.114.97.1", 
                "129.116.84.203"
            ], 
            "workers": [
                "b96990dc35910f0b5e461ac8e2b76e607288f0cb7aff1d7b4896a1e0fd8bb944"
            ]
        }
    }, 
    "status": "success"
}
```
Result: Seems to have worked

Action: Test it out via curl
```
curl -sk -L -X GET "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_03_v0.1/search?transcript=AT1G33930.1&format=json"

{"expression":[{"elem_tissue":"FLOWER","elem_conc":"0.00030","elem_ratio":"0.062","elem_conc2":"0.00017","elem_ratio2":"0.0021","elem_cycle_time":"25.82","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.081"},{"elem_tissue":"IAA","elem_conc":"0.14","elem_ratio":"0.036","elem_conc2":"0.092","elem_ratio2":"0.0012","elem_cycle_time":"25.35","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.34"},{"elem_tissue":"LEAF","elem_conc":"0.057","elem_ratio":"0.040","elem_conc2":"0.035","elem_ratio2":"0.0015","elem_cycle_time":"26.81","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.44"},{"elem_tissue":"NACL","elem_conc":"9.19e-05","elem_ratio":"0.047","elem_conc2":"4.25e-05","elem_ratio2":"0.0015","elem_cycle_time":"25.37","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.63"},{"elem_tissue":"ROOT","elem_conc":"0.00089","elem_ratio":"0.00039","elem_conc2":"0.00031","elem_ratio2":"6.29e-06","elem_cycle_time":"33.43","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.59"},{"elem_tissue":"SALICYLIC","elem_conc":"7.32e-05","elem_ratio":"0.012","elem_conc2":"9.86e-05","elem_ratio2":"0.00085","elem_cycle_time":"26.62","elem_target_id":"AT1G33930.1","elem_cycle_time2":"1.23"},{"elem_tissue":"YOUNG","elem_conc":"1.80e-05","elem_ratio":"0.0048","elem_conc2":"1.37e-05","elem_ratio2":"0.00015","elem_cycle_time":"29.41","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.33"}]}
```
