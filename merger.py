import PyPDF2
import os
import re
from sys import argv

merger = PyPDF2.PdfFileMerger()
file_list = []

if len(argv) == 1:
    name = input('Name: ')
else:
    name = argv[1]

for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        file_list.append(file)

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

sorted = sorted(file_list, key = natural_keys)

for file in sorted:
    merger.append(file)
    print(file)

print('merging, please wait')
merger.write(f"{name}.pdf")