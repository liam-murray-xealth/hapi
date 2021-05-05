#!/usr/bin/env bash

# https://groups.google.com/g/hapi-fhir/c/6aROl3gds2w

BASE='http://localhost:8080/fhir/default'

create_url="$BASE/"'$partition-management-create-partition'

NAME=elsewhere
DESCRIPTION c="St. Elsewhere Hospital"
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

echo $BODY


# curl -vX POST $create_url \
#   -d @partition.json \
#   --header "Content-Type: application/json"
