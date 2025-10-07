# Program to eliminate repeated lines from a file

inputFile = open('FILESAMPLE2.txt', 'r')

outputFile = open('FILESAMPLE2_unique.txt', 'w')

lines_seen_so_far = set()
print("Eliminating duplicate lines...")

for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()

