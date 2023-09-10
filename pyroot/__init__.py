import sys
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def find_root(marker, anchor_path=None, anchor_type=None) -> str:
    anchor_path = _compute_anchor(anchor_path=anchor_path, anchor_type=anchor_type)
    fs_root = anchor_path.root
    curr_dir = anchor_path
    while not curr_dir.samefile(fs_root):
        curr_dir = curr_dir.parent.resolve()
        if (curr_dir / marker).exists():
            return curr_dir
    return None

def set_root(marker, anchor_path=None, anchor_type=None) -> str:
    root = find_root(marker=marker, anchor_path=anchor_path, anchor_type=anchor_type)
    if root:
        sys.path.append(str(root))
        logger.info(f'adding "{root}" to sys.path')
    return root
        

def _compute_anchor(anchor_path=None, anchor_type=None):
    if anchor_path:
        return Path(anchor_path)
    elif anchor_type == 'argv0':
        return Path(sys.argv[0])
    elif anchor_type == 'cwd':
        return Path.cwd()
    else:
        raise Exception(f'unsupported anchor type {anchor_type}')



def script(marker):
    return set_root(marker=marker, anchor='argv0', use_cwd=False)

def notebook(marker):
    return set_root(marker=marker, anchor='cwd')