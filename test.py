import os
test=[]
for file in sorted(os.listdir()):
    if file != "index.html" and file != "scrape.py" and file != "test.py":
        test.append(file)

print(test)
