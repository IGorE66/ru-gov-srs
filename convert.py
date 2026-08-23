#!/usr/bin/env python3
"""
Converts C24Be/AS_Network_List ru-gov blacklists (blacklist-v4.txt / blacklist-v6.txt)
into a sing-box rule-set source JSON, ready for `sing-box rule-set compile`.
"""
import json

def load(path):
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            out.append(line)
    return out

def main():
    v4 = load("blacklist-v4.txt")
    v6 = load("blacklist-v6.txt")

    if not v4 and not v6:
        raise SystemExit("Both blacklist files are empty — aborting, refusing to write an empty rule-set")

    source = {
        "version": 1,
        "rules": [
            {"ip_cidr": v4 + v6}
        ]
    }

    with open("ru-gov-source.json", "w") as f:
        json.dump(source, f, indent=2)

    print(f"Wrote ru-gov-source.json: {len(v4)} IPv4 + {len(v6)} IPv6 ranges")

if __name__ == "__main__":
    main()
