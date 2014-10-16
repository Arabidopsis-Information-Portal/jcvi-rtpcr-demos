
```
curl -sk -L -X POST $API/$NS/services \
    -F "git_repository=https://github.com/mwvaughn/jcvi-rtpcr-demos.git" -F "metadata=expression_per_gene_tissue_04" -H "Authorization: Bearer $TOKEN"
```

