#!/usr/bin/env python
import sys
import re
import json
import os

JSON_COMMIT_TYPE = "commit_type.json"

# Load valid commit types from commit-type.json in the same directory as the script
def load_commit_types():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    json_file_path = os.path.join(script_dir, JSON_COMMIT_TYPE)

    # Read the JSON file and extract commit types
    with open(json_file_path, "r") as f:
        commit_types = json.load(f)
    return [commit_type.lower() for commit_type in commit_types["types"].keys()]

# Regular expression to validate the Conventional Commits format (case insensitive)
def validate_commit_message(message, valid_types):
    # Case insensitive match for commit type
    pattern = r'^(' + '|'.join(valid_types) + r')(\(.+\))?: .{1,50}'
    if re.match(pattern, message, re.IGNORECASE):
        print("Commit message is valid.")
        return True
    else:
        print(f"Commit message is invalid. Valid types are: {', '.join(valid_types)}")
        return False

if __name__ == "__main__":
    valid_commit_types = load_commit_types()
    commit_message = sys.stdin.read().strip()

    if not validate_commit_message(commit_message, valid_commit_types):
        sys.exit(1)
