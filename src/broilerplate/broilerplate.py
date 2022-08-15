from __future__ import annotations

import pathlib
from typing import Optional

import tomli


class InvalidConfigException(Exception):
    pass


class Cmd:

    def __init__(self, cmd) -> None:
        self.cmd = cmd

    def __call__(self) -> None:
        exec(self.cmd)


class Broilerplate:

    def __init__(
        self,
        config: dict,
        config_file: Optional[pathlib.Path] = None,
        config_string: Optional[str] = None,
    ) -> None:
        self.config = config
        self.config_file = config_file
        self.config_string = config_string
        self.__post_init__()

    def __post_init__(self) -> None:
        for k, v in self.config.items():
            if isinstance(v, str):
                self.name = v
            elif isinstance(v, dict):
                setattr(self, k, Cmd(v['cmd']))
            else:
                raise InvalidConfigException

    def __repr__(self) -> str:
        return f'Broilerplate({self.config})'

    def __str__(self) -> str:
        # TODO implement
        return self.__repr__()

    @classmethod
    def _from_file(cls, config_file: str):
        config_path = pathlib.Path(config_file)
        return cls(Broilerplate._parse_config(config_path), config_path)

    @classmethod
    def _from_string(cls, config_string: str):
        return cls(tomli.loads(config_string), config_string=config_string)

    @staticmethod
    def _parse_config(config_file: pathlib.Path):
        """Parse config file
        """
        with open(config_file.absolute(), 'rb') as f:
            config = tomli.load(f)

        return config

    def run(self, config_name: str):
        run_config = self.config[config_name]
        exec(run_config)
