from __future__ import annotations

from broilerplate import __version__
from broilerplate.broilerplate import Broilerplate


def test_version():
    assert __version__ == '0.1.0'


def test_read_config():
    test_config = '''
        name = 'broiltest'

        [footest]
        cmd = "print('foo bar')"
    '''

    broil = Broilerplate._from_string(test_config)
    assert broil.config == {'name': 'broiltest', 'footest': {'cmd': "print('foo bar')"}}
    assert broil.config_file == None
    assert broil.config_string == test_config

def test_run_config(capsys):
    test_config = '''
        name = 'broiltest'

        [footest]
        cmd = "print('hello from footest')"
    '''

    broil = Broilerplate._from_string(test_config)
    broil.footest()  # type: ignore
    captured = capsys.readouterr()
    assert captured.out == 'hello from footest\n'
