import sys
import importlib
import os
sys.path.append('/Users/ophir/dev/pyroot')

from pyroot import set_root
import logging

logger = logging.getLogger(__name__)


def try_import(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except:
        return False
    
def generic_test(marker, anchor_path, expected_modules, unexpected_modules, anchor_type=None):

    if anchor_type is None:
        anchor = anchor_path
    elif anchor_type == 'cwd':
        os.chdir(anchor_path)
        anchor = None
    elif anchor_type == 'argv0':
        sys.argv[0] = anchor_path
        anchor = None


    root = set_root(marker=marker, anchor_path=anchor, anchor_type=anchor_type)
    assert root is not None
    for m in expected_modules:
        assert try_import(m)
    for m in unexpected_modules:
        assert not try_import(m)

def test_regular():
    generic_test(marker='MARKER', 
                 anchor_path='/Users/ophir/dev/pyroot/tests/dummy_root_a/a1/a2/__init__.py', 
                 expected_modules=['a1'], 
                 unexpected_modules=['a2'])

def test_relative_marker():
    generic_test(marker='../MARKER', 
                 anchor_path='/Users/ophir/dev/pyroot/tests/dummy_root_b/b1/b2/__init__.py', 
                 expected_modules=['b2'], 
                 unexpected_modules=['b1'])


def test_cwd():
    generic_test(marker='MARKER', 
                 anchor_path='/Users/ophir/dev/pyroot/tests/dummy_root_a/a1/a2/', 
                 expected_modules=['a1'], 
                 unexpected_modules=['a2'],
                 anchor_type='cwd')

def test_argv():
    generic_test(marker='MARKER', 
                 anchor_path='/Users/ophir/dev/pyroot/tests/dummy_root_a/a1/a2/__init__.py', 
                 expected_modules=['a1'], 
                 unexpected_modules=['a2'],
                 anchor_type='argv0')

