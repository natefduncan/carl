import numpy as np
from dataclasses import dataclass
from dataclasses_json import dataclass_json

def get_dist_by_str(name: str):
    return {
        "normal": Normal,
        "uniform": Uniform,
        "binomial": Binomial,
        "poisson": Poisson,
    }.get(name.lower())

@dataclass_json
@dataclass
class Distribution:
    def sample(self, _rng) -> float:
        return 0

@dataclass_json
@dataclass
class Normal(Distribution):
    mu: float
    sigma: float

    def sample(self, rng):
        return rng.normal(self.mu, self.sigma)

@dataclass_json
@dataclass
class Uniform(Distribution):
    low: float
    high: float

    def sample(self, rng):
        return rng.uniform(self.low, self.high)

@dataclass_json
@dataclass
class Binomial(Distribution):
    n: float
    p: float

    def sample(self, rng):
        return rng.binomial(self.n, self.p)

@dataclass_json
@dataclass
class Poisson(Distribution):
    lam: float

    def sample(self, rng):
        return rng.poisson(self.lam)
