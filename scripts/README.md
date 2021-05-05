# Scripts

## Install requirements

Create a virtual env and install requirements

```bash
pip install -r requirements.txt
```

## Partitions

Edit partition.py and set the base URL, e.g.:

```bash
BASE='http://localhost:8080/fhir/default'
```

Or set in env

```bash
export BASE_URL=http://localhost:8080/fhir/default
```

### Example

Edit partition.py to add or update partion names and mappings

```bash
partition.py create -n general
```
