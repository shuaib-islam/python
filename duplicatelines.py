outputfile = open('codingalupdate.txt', 'w')
inputfile = open('codingal.txt', 'r')

line_seen_so_far = set()

print("Eliminating duplicate lines")

for line in inputfile:
    
    if not line_seen_so_far:
        
        outputfile.write(line)
        line_seen_so_far.add(line)
        
inputfile.close()
outputfile.close()