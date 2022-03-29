#text_file = open("analysis/theater4.txt")

text_file=""
with open('analysis/theater4.txt','r') as file:
    for line in file:
        text_file+=line.strip()+"\n"
        text_file+=line.strip()+"s\n"
        text_file+=line.strip()+"es\n"
    file.close()
with open('analysis/theater4.txt','w') as file:
    file.write(text_file)
    file.close()


bok1 = open('analysis/theater4.txt','r')
bok = bok1.read().split('\n')
for i in range(len(bok)): #lowercase each bok term
  bok[i] = bok[i].lower()
# bok = text_file.read().split('\n')
# for i in range(len(bok)): #lowercase each bok term
#   bok[i] = bok[i].lower()

