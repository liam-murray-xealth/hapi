#!/usr/bin/env bash

# https://groups.google.com/g/hapi-fhir/c/6aROl3gds2w

BASE='http://localhost:8080/fhir/default'

create_url="$BASE/"'$partition-management-create-partition'

NAME=elsewhere
DESCRIPTION="St. Elsewhere Hospital"
ID=124

read -r -d '' BODY <<EOF
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "id",
      "valueInteger": $ID
    },
    {
      "name": "name",
      "valueCode": "$NAME"
    },
    {
      "name": "description",
      "valueString": "$DESCRIPTION"
    }
  ]
}
EOF

echo "===> Sending"
echo
echo $BODY
echo
echo "<=== Response"
echo

# -d @partition.json \

curl $create_url \
  -d "$BODY" \
  --header "Content-Type: application/json"
