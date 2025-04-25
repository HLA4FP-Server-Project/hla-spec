#!/bin/env python3
from pathlib import Path
import sys

def main():
    root_path = Path(".")
    # Parse arguments and validate them
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} hla_version")
        print("Note, hla_version must match the name of a folder")
        return
    hla_version = sys.argv[1]
    hla_path = root_path / hla_version
    if not hla_path.exists():
        print(f"{hla_path.absolute()}: File does not exist")
        return
    if not hla_path.is_dir():
        print(f"{hla_path.absolute()}: Not a directory")
        return
    print(f"Compiling {hla_path.absolute()}")

    # Generate a pom
    template = read_file_as_str(root_path / "pom-template.xml")
    template = template.replace("$$hla$$", hla_version)
    template = template.replace("$$attribution$$", read_file_as_str(hla_path / "attribution.txt"))
    if not (hla_path / "pom.xml").exists():
        (hla_path / "pom.xml").touch()
    with open(hla_path / "pom.xml", "w") as target:
        _ = target.write(template)
    print("Generated POM")

def read_file_as_str(p: Path) -> str:
    with open(p, "r") as f:
        return f.read()

if __name__ == "__main__":
    main()