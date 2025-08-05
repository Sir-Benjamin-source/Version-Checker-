#!/usr/bin/env python3

import argparse
import hashlib
import json
import os
import sys  # Added for debugging
from datetime import datetime

def generate_stamp(citation):
    """Generate a unique stamp suffix like #CS-RefX (X from hash)."""
    hash_obj = hashlib.md5(citation.encode())
    hash_char = hash_obj.hexdigest()[0].upper()
    return f"#CS-Ref{hash_char}"

def format_citation(citation, style="standard"):
    """Format citation based on style."""
    if style == "standard":
        return f"Citation: {citation} (Generated on {datetime.now().strftime('%Y-%m-%d')})"
    elif style == "poetic":
        parts = citation.split(", ")
        return f"In code's grand weave, {parts[0]} does conceive; With {parts[1]}'s lore, we forevermore. ({parts[2] if len(parts) > 2 else ''})"
    elif style == "minimal":
        return f"Cit: {citation}"
    else:
        raise ValueError("Invalid style: choose standard, poetic, or minimal.")

def main():
    # Debug: Print raw command-line args
    print(f"Raw sys.argv: {sys.argv}")
    
    parser = argparse.ArgumentParser(description="Version Checker+: Hyperlink Stamp Generator for Self-Documenting Versions")
    parser.add_argument("version", help="Software version, e.g., v1.1")
    parser.add_argument("directory", help="Notes file path (JSON), e.g., notes.json")
    parser.add_argument("citation", help="Citation string, e.g., 'John Smith, Spiral Theory, DOI: 10.5281/zenodo.16585562'")
    parser.add_argument("--style", default="standard", choices=["standard", "poetic", "minimal"], help="Citation style")
    parser.add_argument("--patch", default="Initial entry", help="Patch notes for this version")
    parser.add_argument("--write", action="store_true", help="Write/update the notes file")
    
    args = parser.parse_args()

    stamp = generate_stamp(args.citation)
    stamped_version = f"{args.version}{stamp}"
    formatted_citation = format_citation(args.citation, args.style)

    entry = {
        "version": args.version,
        "patch": args.patch,
        "citation": formatted_citation,
        "timestamp": datetime.now().isoformat()
    }

    print(f"Stamped Version: {stamped_version}")
    print(f"Linking to: {args.directory}")
    print("Generated Entry:")
    print(json.dumps(entry, indent=2))

    if args.write:
        data = {}
        if os.path.exists(args.directory):
            with open(args.directory, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Warning: {args.directory} is not a valid JSON file; overwriting with new data.")
        data[args.version] = entry
        with open(args.directory, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Updated {args.directory} with new entry.")

if __name__ == "__main__":
    main()
