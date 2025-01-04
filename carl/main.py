import click
import json
import csv
import sys

from carl.config import Config
from carl.model import Model
from carl.simulation import Simulation

@click.group
def cli():
    pass

def dict_to_rows(results):
    # Headers
    headers = ["i"] + list(results[0]["assumptions"].keys()) 
    for k, v in results[0]["outputs"].items():
        for i in range(len(v)):
            for j in range(len(v[0])):
                headers.append(f"{k}.{i}.{j}")

    # Values
    rows = [headers]
    for result in results:
        row = [result["i"]] + list(result["assumptions"].values())
        for v in result["outputs"].values():
            for i in v:
                for j in i:
                    row.append(j)
        rows.append(row)
    return rows

@click.argument("model-path")
@click.option("-c", "--config-path", default="default.toml")
@click.option("-n", "--nreps", default=1000)
@click.option("-f", "--output-format", default="json", help="json,csv")
@cli.command
def simulate(model_path, config_path, nreps, output_format):
    model = Model(model_path)
    model.load()
    config = Config.from_path(config_path)
    sim = Simulation(model, config, nreps)
    sim.run()
    results = sim.to_dict()["results"]
    if output_format == "json":
        click.echo(json.dumps(results))
    elif output_format == "csv":
        rows = dict_to_rows(results)
        writer = csv.writer(sys.stdout)
        writer.writerows(rows)

if __name__=="__main__":
    cli()
