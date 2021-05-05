#!/usr/bin/env python3
#
# See:
#   https://hapifhir.io/hapi-fhir/docs/server_jpa_partitioning/partitioning_management_operations.html
#
import json
import requests
import click
import os

# Hit the default partition to create/update deployment
BASE=os.environ.get('BASE_URL') or 'http://localhost:8080/fhir/default'

def make_request_body(ident, name, description):
    return {
    "resourceType": "Parameters",
    "parameter": [
      {
        "name": "id",
        "valueInteger": ident
      },
      {
        "name": "name",
        "valueCode": name
      },
      {
        "name": "description",
        "valueString": description
      }
    ]
  }

def confirm_post(url, body):
  if click.confirm('\nContinue?', default=False):
    res = requests.post(url, json=body)
    print(res.status_code)
    print(res.json())

def create_part(entry):
  (name, ident, description) = entry
  body = make_request_body(ident, name, description)
  url = f'{BASE}/$partition-management-create-partition'
  print(f"Create partition {name}/{ident} via {url}")
  confirm_post(url, body)

def update_part(entry):
  (name, ident, description) = entry
  body = make_request_body(ident, name, description)
  url = f'{BASE}/$partition-management-update-partition'
  print(f"Update partition {name}/{ident} via {url}")
  confirm_post(url, body)

def delete_part(entry):
  (name, ident, description) = entry
  body = make_request_body(ident, name, description)
  url = f'{BASE}/$partition-management-delete-partition'
  print(f"Delete partition {name}/{ident} via {url}")
  confirm_post(url, body)

parts = {a[0]:a for a in [
  ("general", 10, "General Hospital"),
  ("elsewhere", 11, "Elsewhere")
]}

@click.group()
def cli():
  pass

@click.command()
@click.option('-n', '--name', required=True, help="Partition name", type=click.Choice(parts.keys()))
def create(name):
  create_part(parts.get(name))

@click.command()
@click.option('-n', '--name', required=True, help="Partition name", type=click.Choice(parts.keys()))
def update(name):
  update_part(parts.get(name))

@click.command()
@click.option('-n', '--name', required=True, help="Partition name", type=click.Choice(parts.keys()))
def delete(name):
  delete_part(parts.get(name))

@click.command()
def info():
  print(f"Base URL is {BASE}")


cli.add_command(info)
cli.add_command(create)
cli.add_command(update)
cli.add_command(delete)

if __name__ == "__main__":
  cli()  # pylint: disable=no-value-for-parameter
