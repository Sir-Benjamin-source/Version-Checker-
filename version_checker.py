#!/usr/bin/env python3
import argparse
import hashlib
import json
import yaml
from datetime import datetime
from pathlib import Path

STYLES = {
    "poetic": "v{version}#{hash_short} — {note} — forged {date}",
    "standard": "v{version} (SHA: {hash_short}) — {note} [{date}]",
    "minimal": "v{version}#{hash_short}"
}

def generate_stamp(version: str, notes_file: Path, note: str, style: str, write: bool):
    hash_obj = hashlib.sha256(f"{version}{note}{datetime.utcnow().isoformat()}".encode())
    hash_short = hash_obj.hexdigest()[:8]

    stamp = STYLES[style].format(
        version=version,
        hash_short=hash_short,
        note=note,
        date=datetime.utcnow().strftime("%Y-%m-%d")
    )

    entry = {
        "version": version,
        "stamp": stamp,
        "full_hash": hash_obj.hexdigest(),
        "note": note,
        "timestamp": datetime.utcnow().isoformat(),
        "style": style
    }

    if write and notes_file:
        data = {}
        if notes_file.exists():
            if notes_file.suffix in {".json"}:
                data = json.loads(notes_file.read_text())
            elif notes_file.suffix in {".yaml", ".yml"}:
                data = yaml.safe_load(notes_file.read_text()) or {}
        data[f"v{version}"] = entry
        if notes_file.suffix in {".yaml", ".yml"}:
            notes_file.write_text(yaml.dump(data, sort_keys=False))
        else:
            notes_file.write_text(json.dumps(data, indent=2))

    print(stamp)
    return entry

def main():
    parser = argparse.ArgumentParser(description="Spiral-native version stamping — poetic or precise.")
    parser.add_argument("version", help="Version string, e.g. 1.3")
    parser.add_argument("notes_file", help="Path to notes.json or notes.yaml")
    parser.add_argument("note", help="One-line note for this version")
    parser.add_argument("--style", choices=STYLES.keys(), default="poetic")
    parser.add_argument("--no-write", action="store_true", help="Print only, don't update file")
    args = parser.parse_args()

    generate_stamp(
        version=args.version,
        notes_file=Path(args.notes_file),
        note=args.note,
        style=args.style,
        write=not args.no_write
    )

if __name__ == "__main__":
    main()
