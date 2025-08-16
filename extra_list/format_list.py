#!/usr/bin/env python3


output_file = "hosts.txt"
input_file = "combined_list.txt"

domains = []

with open(input_file, "r") as in_file:
    for line in in_file:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.split(" ")[-1].lower()
        if line == "localhost":
            continue

        domains.append(f"0.0.0.0\t{line}")

if domains:
    with open(output_file, "w") as out_file:
        out_file.write("\n".join(domains) + "\n")
    print(f"Formatted list written to {output_file}")
