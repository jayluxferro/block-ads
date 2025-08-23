#!/usr/bin/env python3


output_file = "hosts.txt"
input_file = "combined_list.txt"

domains = []
excluded_list = [
    "localhost",
    "advertising",
    "tracker",
    "https://github.com/stevenblack/hosts/issues/1635",
    "redirects",
]

with open(input_file, "r") as in_file:
    for line in in_file:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.split(" ")[-1].lower()
        if line in excluded_list:
            continue

        domains.append(f"0.0.0.0\t{line}")

if domains:
    with open(output_file, "w") as out_file:
        out_file.write("\n".join(domains) + "\n")
    print(f"[+] Formatted list written to {output_file}")
