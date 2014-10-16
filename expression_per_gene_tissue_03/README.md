Expression_per_gene_tissue_03: Generic
======================================

An example of how to configure a simple genericAPI under ADAMA. One passes a GET requesting a specific "locus" to the $API/$NS/$SERVICE_$VERSION/search endpoint. The result is fetched and returned. This example demonstrates excellent manual error handling and parameter validation.

Action: Enroll via Gitrepo
```
curl -sk -L -X POST $API/$NS/services -F "git_repository=https://github.com/mwvaughn/jcvi-rtpcr-demos.git" -F "metadata=expression_per_gene_tissue_03" -H "Authorization: Bearer $TOKEN"
```
