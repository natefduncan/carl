import click

from carl.config import Config
from carl.model import Model
from carl.simulation import Simulation

@click.group
def cli():
    pass

@click.argument("model-path")
@click.option("-c", "--config-path", default="default.toml")
@click.option("-n", "--nreps", default=1000)
@cli.command
def simulate(model_path, config_path, nreps):
    model = Model(model_path)
    model.load()
    config = Config.from_path(config_path)
    sim = Simulation(model, config, nreps)
    sim.run()
    print(sim.results)

if __name__=="__main__":
    cli()
