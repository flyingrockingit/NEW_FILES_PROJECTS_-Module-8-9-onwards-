with open("FILESAMPLE2.txt", "r") as fp:
    data1 = fp.read()

with open("FILESAMPLE2_unique.txt", "r") as fp:
    data2 = fp.read()

if not data1.endswith("\n"):
    data1 += "\n"

merged_data = data1 + data2

print("Merging two files...")

with open("MergedFile.txt", "w") as fp:
    fp.write(merged_data)

print("Merged file created successfully: MergedFile.txt")
