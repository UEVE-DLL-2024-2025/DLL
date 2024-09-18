#!/usr/bin/env python
"""
This script validates commit messages based on the Conventional Commits specification.
It ensures that commit messages follow a predefined format defined in commit_type.json.
"""

import sys
import re
import json
import os

JSON_COMMIT_TYPE = "commit_type.json"

def load_commit_types():
    """
    Load valid commit types from the commit_type.json file located in the same directory as
    the script.

    Returns:
        list: A list of valid commit types in lowercase.
    """
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    json_file_path = os.path.join(script_dir, JSON_COMMIT_TYPE)

    # Read the JSON file and extract commit types
    with open(json_file_path, "r", encoding="utf-8") as file:
        commit_types = json.load(file)
    return [commit_type.lower() for commit_type in commit_types["types"].keys()]

def validate_commit_message(message, valid_types):
    """
    Validate the commit message based on the given valid types and Conventional Commits format.

    Args:
        message (str): The commit message to validate.
        valid_types (list): A list of valid commit types.

    Returns:
        bool: True if the commit message is valid, False otherwise.
    """
    # Case insensitive match for commit type
    pattern = r'^(' + '|'.join(valid_types) + r')(\(.+\))?: .{1,50}'
    if re.match(pattern, message, re.IGNORECASE):
        print("Commit message is valid.")
        return True

    print(f"Commit message ({message}) is invalid. Valid types are: {', '.join(valid_types)}")
    return False

if __name__ == "__main__":
    valid_commit_types = load_commit_types()
    commit_message = sys.stdin.read().strip()

    if not validate_commit_message(commit_message, valid_commit_types):
        sys.exit(1)
