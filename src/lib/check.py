from pathlib import Path

def check_path(path: Path = None, verbose: int = 0) -> bool:
    if path is None:
        return False        
    check = path.exists()
    if verbose != 0:
        if check:
            print(f"Path {path} exists!")
        else:
            print(f"Path {path} does not exist!")
    return check

def check_paths():
    script_dir = Path(__file__).resolve().parents[1]

    lib_path = script_dir / "lib"
    data_path = script_dir / "../data" 
    out_path = script_dir / "../out"

    data_path = data_path.resolve()
    out_path = out_path.resolve()

    checks = [
        check_path(lib_path, verbose=0),
        check_path(data_path, verbose=0),
        check_path(out_path, verbose=0),
    ]

    if all(checks):
        print("Check completed!")
        paths = {}
        paths["lib_path"] = lib_path
        paths["data_path"] = data_path
        paths["out_path"] = out_path
        return paths 
    else:
        print("Some paths are not loaded!")
        if not checks[0]: print(f"Missing: {lib_path}")
        if not checks[1]: print(f"Missing: {data_path}")
        if not checks[2]: print(f"Missing: {out_path}")

if __name__ == "__main__":
    check_paths()