from dataclasses import dataclass, field
from typing import List, Dict, Any
import numpy as np
from tqdm import tqdm

from carl.model import Model
from carl.config import Config

@dataclass
class Iteration:
    i: int
    assumptions: Dict[str, float] = field(default_factory=dict)
    outputs: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Simulation:
    model: Model
    config: Config
    nreps: int
    results: List[Iteration] = field(default_factory=list)
    
    def run(self):
        rng = np.random.default_rng()
        for i in tqdm(range(self.nreps)):
            iteration = Iteration(i)

            # Assumptions
            for a in self.config.assumptions:
                new_value = a.distribution.sample(rng)
                self.model.set_sheet_value(a.sheet, a.range, new_value)
                iteration.assumptions[a.name] = new_value

            self.model.evaluate()

            # Outputs
            for o in self.config.outputs:
                values = self.model.get_sheet_values(o.sheet, o.range)
                iteration.outputs[o.name] = values
            self.results.append(iteration)
