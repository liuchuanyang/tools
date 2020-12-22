# import config
index=100
# f=open("config.py", "w+")
leng=0
with open("config.py", "r+") as f:
    line_list=[line for line in f ]
    for line in line_list[:6]:
        leng+=len(line)
    f.seek(0,0)
    f.seek(leng)
    f.write("index=%d"%(200))