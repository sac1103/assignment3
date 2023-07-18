"""Place the "PYTHON.txt" file in the same directory as this Python script.
 Run the program, and it will generate a new file "PYTHON1.txt" with
 the extracted alphanumeric characters.
 """

import io
from io import open

with io.open("python.txt","r",encoding="utf-8") as fh:
    with io.open("python1.txt","w",encoding="utf-8") as fw:
        rec=fh.read()
for a in rec:
    if not a.isdigit():
        print(a,end=' ')
        fw.write(a)
fh.close()
fw.close()
