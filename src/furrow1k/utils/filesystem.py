from pathlib import Path


def get_project_root() -> Path:
    """
    Returns project root (this file must be in `project_root/utils/` or 
    equivalent.
    """
    result = Path(__file__).parent.parent.parent.parent

    return result


def get_filepath(
    fname: str, fpath: str | Path = None, suffix: str = ".txt"
) -> str:
    if fpath is None:
        fpath = get_project_root() / "data" / "ascii"
    elif isinstance(fpath, str):
        fpath = Path(fpath)
    
    if fpath.suffix != suffix:
        fpath = fpath / fname

    return fpath


def load_text(fname: str, fpath: str | Path = None) -> str:
    fpath = get_filepath(fname, fpath)
    
    with open(fpath, "r") as f:
        result = f.read()

    return result

    
def load_text_lines(fname: str, fpath: str | Path = None) -> list[str]:
    fpath = get_filepath(fname, fpath)
    
    with open(fpath, "r") as f:
        result = f.readlines()

    return result

    