from typing import List
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
import tomllib

from carl.distribution import get_dist_by_str, Distribution

@dataclass_json
@dataclass
class Assumption:
    name: str
    sheet: str
    range: str
    distribution: Distribution
    
    @classmethod
    def from_data(cls, data):
        d = data["distribution"]
        d_class = get_dist_by_str(d["name"])
        d.pop("name")
        data["distribution"] = d_class(**d)
        return cls(**data)

@dataclass_json
@dataclass
class Output:
    name: str
    sheet: str
    range: str

    @classmethod
    def from_data(cls, data):
        return cls(**data)

@dataclass_json
@dataclass
class Config:
    name: str
    assumptions: List[Assumption] = field(default_factory=list)
    outputs: List[Output] = field(default_factory=list)

    @classmethod
    def from_path(cls, path: str):
        with open(path, "rb") as f:
            data = tomllib.load(f)
        return Config.from_data(data) 

    @classmethod
    def from_data(cls, data):
        name = data.get("name")
        assumptions = [Assumption.from_data(i) for i in data["assumptions"]]
        outputs = [Output.from_data(i) for i in data["outputs"]]
        return cls(name, assumptions, outputs)
