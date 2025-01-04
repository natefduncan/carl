import click
import json

from carl.config import Config
from carl.model import Model
from carl.simulation import Simulation

@click.group
def cli():
    pass

@click.argument("model-path")
@click.option("-c", "--config-path", default="default.toml")
@click.option("-n", "--nreps", default=1000)
@click.option("-f", "--format", default="json")
@cli.command
def simulate(model_path, config_path, nreps, format):
    model = Model(model_path)
    model.load()
    config = Config.from_path(config_path)
    sim = Simulation(model, config, nreps)
    sim.run()
    results = sim.to_dict()["results"]
    click.echo(json.dumps(results))

if __name__=="__main__":
    cli()
