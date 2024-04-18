import subprocess as sb
with open(r"E:\nmap_output.txt", 'w') as ou:
    sb.run('nmap -sS -p 22,80 scanme.nmap.org', shell = True,text=True, stdout=ou)
print("Getting data from the file")
with open(r"E:\nmap_output.txt", 'r') as i: print(i.read()) 