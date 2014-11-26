Expression_condition_comparison: Query x AIP native response
==========================================================

An example of how to configure a simple query API under ADAMA. One passes a GET requesting a specific "foldchange" increase in expression in "material1" over "material2" to the $API/$NS/$SERVICE_$VERSION/search endpoint. The result is fetched and returned as a prototypical AIP JSON document.

Action: Enroll via Gitrepo
```
curl -sk -L -X POST $API/$NS/services -F \
    "git_repository=https://github.com/Arabidopsis-Information-Portal/jcvi-rtpcr-demos.git" \
    -F "metadata=expression_condition_comparison" \
    -H "Authorization: Bearer $TOKEN"
```

Action: Test service
```
curl -sk -L -X GET "$API/$NS/expression_condition_comparison_v0.1/search?material1=flower&material2=root&foldchange=5" \
    -H "Authorization: Bearer $TOKEN" \
    | python -mjson.tool

```
