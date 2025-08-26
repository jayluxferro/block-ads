#!/usr/bin/env python3
import re

output_file = "hosts.txt"
input_file = "combined_list.txt"

domain_regex = re.compile(
    r"^(?!-)"  # Ensure it does not start with a hyphen
    r"(?!.*\.$)"  # Ensure it does not end with a dot
    r"(?!.*\.\.)"  # Ensure it does not have consecutive dots
    r"(?!.*(?:^|\.)[0-9]+\.(?:[0-9]+\.)*[0-9]+$)"  # Ensure it is not an IP address format
    r"[A-Za-z0-9-_]+"  # One or more alphanumeric characters, hyphens, or underscores
    r"(?:\.[A-Za-z0-9-_]+)+"  # One or more domain labels separated by dots
    r"$",  # End of the string
    re.IGNORECASE,  # Case-insensitive matching
)

domains = []
excluded_list = [
    "localhost",
    "advertising",
    "tracker",
    "https://github.com/stevenblack/hosts/issues/1635",
    "redirects",
    "malware",
    "tracking",
    "code]",
    "tracker]",
    "network]",
]

funny_chars = [
    "[",
    "]",
    "#",
]

with open(input_file, "r") as in_file:
    for line in in_file:
        line = line.strip()
        if not line:
            continue

        skip = False
        for char in funny_chars:
            if char in line:
                skip = True
                break

        line = line.split(" ")[-1].lower().strip()
        if line in excluded_list:
            continue

        if not skip and domain_regex.match(line):
            blacklisted_domain = f"0.0.0.0\t{line}"
            try:
                domains.index(blacklisted_domain)
            except Exception:
                domains.append(blacklisted_domain)

if domains:
    with open(output_file, "w") as out_file:
        out_file.write("\n".join(domains) + "\n")
    print(f"[+] Formatted list written to {output_file}")
