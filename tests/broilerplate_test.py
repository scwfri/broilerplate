from __future__ import annotations

from broilerplate import __version__
from broilerplate.broilerplate import Broilerplate


def test_version():
    assert __version__ == '0.1.0'


def test_read_cgf():
    test_cfg = '''
        name = 'broiltest'

        [broil.test1]
        testbroil = "print('foo bar')"
    '''

    broil = Broilerplate._from_string(test_cfg)
    assert broil.config == {'name': 'broiltest', 'broil': {'test1': {'testbroil': "print('foo bar')"}}}
    assert broil.config_file == None
    assert broil.config_string == test_cfg
