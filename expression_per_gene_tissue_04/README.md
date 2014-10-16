
```
# Enroll via Gitrepo
curl -sk -L -X POST $API/$NS/services -F "git_repository=https://github.com/mwvaughn/jcvi-rtpcr-demos.git" -F "metadata=expression_per_gene_tissue_04" -H "Authorization: Bearer $TOKEN"
# Bugs out. We're fixing this

# Enroll via POSTed options
curl -sk -L -X POST $API/$NS/services \
     -F "name=expression_per_gene_tissue_04" -F "description=JCVI RTPCR Webservice Pass-Through" -F "type=passthrough" -F "url=http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue" -H "Authorization: Bearer $TOKEN"

# Result... seems to work
{
    "message": "registration started", 
    "result": {
        "list_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_04_v0.1/list", 
        "notification": "", 
        "search_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_04_v0.1/search", 
        "state_url": "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_04_v0.1"
    }, 
    "status": "success"
}

# Status check
curl -sk -L -X GET "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_04_v0.1"

# Result. Looks good
{
    "result": {
        "service": {
            "code_dir": null, 
            "description": "JCVI RTPCR Webservice Pass-Through", 
            "json_path": "", 
            "main_module": "main", 
            "metadata": "", 
            "name": "expression_per_gene_tissue_04", 
            "namespace": "vaughn-dev", 
            "notify": "", 
            "requirements": [], 
            "type": "passthrough", 
            "url": "http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue", 
            "version": "0.1", 
            "whitelist": [
                "www.jcvi.org", 
                "129.114.97.1", 
                "129.114.97.2", 
                "129.116.84.203"
            ]
        }
    }, 
    "status": "success"
}

# Testing time

curl -sk -L -X GET "https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/expression_per_gene_tissue_04_v0.1/search?gene=AT1G33930.1&format=json&Submit=Search"

# Works
{"expression":[{"elem_tissue":"FLOWER","elem_conc":"0.00030","elem_ratio":"0.062","elem_conc2":"0.00017","elem_ratio2":"0.0021","elem_cycle_time":"25.82","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.081"},{"elem_tissue":"IAA","elem_conc":"0.14","elem_ratio":"0.036","elem_conc2":"0.092","elem_ratio2":"0.0012","elem_cycle_time":"25.35","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.34"},{"elem_tissue":"LEAF","elem_conc":"0.057","elem_ratio":"0.040","elem_conc2":"0.035","elem_ratio2":"0.0015","elem_cycle_time":"26.81","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.44"},{"elem_tissue":"NACL","elem_conc":"9.19e-05","elem_ratio":"0.047","elem_conc2":"4.25e-05","elem_ratio2":"0.0015","elem_cycle_time":"25.37","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.63"},{"elem_tissue":"ROOT","elem_conc":"0.00089","elem_ratio":"0.00039","elem_conc2":"0.00031","elem_ratio2":"6.29e-06","elem_cycle_time":"33.43","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.59"},{"elem_tissue":"SALICYLIC","elem_conc":"7.32e-05","elem_ratio":"0.012","elem_conc2":"9.86e-05","elem_ratio2":"0.00085","elem_cycle_time":"26.62","elem_target_id":"AT1G33930.1","elem_cycle_time2":"1.23"},{"elem_tissue":"YOUNG","elem_conc":"1.80e-05","elem_ratio":"0.0048","elem_conc2":"1.37e-05","elem_ratio2":"0.00015","elem_cycle_time":"29.41","elem_target_id":"AT1G33930.1","elem_cycle_time2":"0.33"}]}

# Look for CORS support. Not yet but ASAP

```

