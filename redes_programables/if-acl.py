devices = [ "R1", "R2", "R3", "S1", "S2" ]

switches = []

for item in devices:
    if "1" in item:
        switches.append(item)

print(switches)
