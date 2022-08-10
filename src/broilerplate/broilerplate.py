from __future__ import annotations

import pathlib
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

import tomli


@dataclass
class Broilerplate:
    config: dict
    config_file: Optional[pathlib.Path] = field(default=None)
    config_string: Optional[str] = field(default=None)

    @classmethod
    def _from_file(cls, broil_file):
        return cls(Broilerplate._parse_config(pathlib.Path(broil_file)), config_file=broil_file)

    @classmethod
    def _from_string(cls, broil_string):
        return cls(tomli.loads(broil_string), config_string=broil_string)

    @staticmethod
    def _parse_config(broil_pan):
        """Parse broil pan configuration
        """
        with open(broil_pan.absolute(), 'rb') as f:
            pan = tomli.load(f)

        return pan
