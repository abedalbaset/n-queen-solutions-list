#convert n queen square solution to lines

# global change according to file
boardlenghth=12
file_name="12_12_sol.txt"
outputfilename="12_12_lines.txt"
#end global change according to file

with open(file_name) as f:
    content = f.readlines()

content = [x.strip() for x in content]

numberofsol=len(content)/(boardlenghth+2)
f = open(outputfilename, "a")

for c in range(1,len(content),boardlenghth+2):
    sum=""
    for cc in range(0,boardlenghth):
        sum=sum+content[c+cc]+"  "
    f.write(sum+"\n")
f.close()
