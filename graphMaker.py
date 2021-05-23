import matplotlib.pyplot as plt
import os
import pandas as pd
import shutil

def barGraph(x,y,title,labelx,labely,filename):
    plt.bar(x,y)
    plt.title(title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.savefig(filename,dpi=300)

def lineGraph(x,y,title,labelx,labely,filename):
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.savefig(filename,dpi=300)

def pngFileName(title):
    l = title.split()
    png = ""
    for x in l:
        png += x.capitalize()

    return png

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))


heading1 = "2D PLOT by Shayan"
heading2 = "==============================================================================="
heading3 = "This console application will generate 2D graph for the data you will enter"

print()
print()
print_centre(heading1)
print_centre(heading2)
print_centre(heading3)
print_centre(heading2)
print()
print()

cordinateQty = int(input("Enter the total number of cordinates : "))
print()
title = input("Enter the title of your graph = ")
print()
labelx = input("Enter the label of x-axis = ")
print()
labely = input("Enter the label of y-axis = ")
print()

if len(labelx) == 0:
    labelx = "Label-x"

if len(labely) == 0:
    labely = "Label-y"

if len(title) == 0:
    title = "Title of graph"

x = []
y = []

i=0
print("Enter cordinates below")
print()
while i<cordinateQty:
    print(f"For cordinate {i+1}")
    print("---------------------")
    xval = float(input("x = "))
    x.append(xval)
    yval = float(input("y = "))
    y.append(yval)
    print()
    i=i+1

# ALTERNATE METHOD OF TAKING INPUTS OF CORDINATES
# ------------------------------------------------
# xvals = []
# yvals = []

# print(f"Enter values of x or {labelx} seperated by space")
# xvals = input().split()
# x = list(map(toFloat, xvals))

# print(f"Enter values of y or {labely} seperated by space")
# yvals = input().split()
# y = list(map(toFloat, yvals))

filenameForBar = pngFileName(title) + "_barGraph.png"
filenameForLine = pngFileName(title) + "_lineGraph.png"

userData = {labelx:x, labely:y}
df = pd.DataFrame(userData)
xlFileName = pngFileName(title)+".xlsx"
df.to_excel(xlFileName,index=False)

option = 't'
options = ['1','2','3']
os.system("cls")

while option not in options:
    print("What type of graph do you want to create?")
    print("1. Line graph")
    print("2. Bar graph")
    print("3. Both")
    print()
    option = input("Choose your option = ")
    print()
    if option == '1':
        lineGraph(x,y,title,labelx,labely,filenameForLine)
    elif option == '2':
        barGraph(x,y,title,labelx,labely,filenameForBar)
    elif option == '3':
        lineGraph(x,y,title,labelx,labely,filenameForLine)
        barGraph(x,y,title,labelx,labely,filenameForBar)
    else:
        os.system("cls")
        print("Please enter appropriate option")
    print()


print("Wrong input")

os.system("cls")
heading1 = "==============================================================================="
heading2 = "Your graph generated successfully"

print()
print()
print_centre(heading1)
print_centre(heading2)
print_centre(heading1)
print()
print()

print("Thanks for using")
input("Press ANY KEY to exit")