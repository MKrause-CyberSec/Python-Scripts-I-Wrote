'''Develop a program that reads students’ grades from a file named
“studentdata.txt’, and writes their names and average into a new file named
“studentaverage.txt’. Round the numbers to the closest integer.
The following sample file called studentdata.txt contains one line for
each student in an imaginary class. The student’s name is the first thing on each
line, followed by some exam scores. The number of scores might be different for each student.
'''

infile = open('studentdata.txt',"r")          #I know you showed us using a function
outfile = open('studentaverage',"w")          #being my first time coding files I found this way easier
aline = infile.readline()                     #it is very similar to the one in the book

while aline:                                  #I used a function on the next problem
    sum = 0
    items = aline.split()
    scores = items[1:]
    for i in scores:
        sum = sum + int(i)
    total = sum//len(scores)
    dataline = items[0] + ',' + str(total)
    outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()

