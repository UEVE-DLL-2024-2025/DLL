#!/usr/bin/env python
import sys
import re
import json
import os

# Load valid commit types from commit-type.json in the same directory as the script
def load_commit_types():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Build the full path to the commit-type.json file
    json_file_path = os.path.join(script_dir, "commit_type.json")

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
    # Load commit types from commit-type.json
    valid_commit_types = load_commit_types()

    # Check if commit message is passed via stdin or as a file argument
    if not sys.stdin.isatty():  # Commit message provided via pipe
        commit_message = sys.stdin.read().strip()
    elif len(sys.argv) > 1:  # Commit message provided via file argument
        commit_msg_file = sys.argv[1]
        with open(commit_msg_file, 'r') as f:
            commit_message = f.read().strip()
    else:
        print("Error: No commit message provided.")
        sys.exit(1)

    # Validate the commit message
    if not validate_commit_message(commit_message, valid_commit_types):
        sys.exit(1)
