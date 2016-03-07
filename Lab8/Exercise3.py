#-------------------------------------------------------------------------------
# Name:        Lab 8-Exercise 3
# Purpose:
#
# Author:      Zhao
#
# Created:     07/03/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getSummary(data):
    dataSet = []
    marks = []
    numbers = [0]*10
    min = 100
    max = 0
    for i in data.readlines():
        mark = int(i.split()[1])
        marks.append(mark)
        if mark >= max:
            max = mark
        if mark <= min:
            min = mark
        for i in range(10):
            if mark <= i*10+9 and mark >= i*10:
                numbers[i]+=1
    average = sum(marks)/len(marks)
    return[average,min,max,numbers]

def writeHead(html,data):
    average = '<p>Average is: '+str(data[0])+'</p>'
    min = '<p>Minimum is: '+str(data[1])+'</p>'
    max = '<p>Maximum is: '+str(data[2])+'</p>'
    html.write('<!doctype html>')
    html.write('<html>')
    html.write('<head>')
    html.write('<meta charset="utf-8">')
    html.write('<title>Exercise3</title>')
    html.write('</head>')
    html.write('<body>')
    html.write('<h1>Welcome to statistics page!</h1>')
    html.write(average)
    html.write(min)
    html.write(max)
    html.write('<table>')
    html.write('<tr>')


def writeHTML(data):
    html = open('exercise.html','w')
    numbers = data[3]
    groups = []
    for i in range(10):
        temp = '['+str(i)+'-'+str(i*10+9)+']'
        groups.append(temp)
    writeHead(html,data)
    for i in numbers:
        html.write('<td valign="bottom" style="width:25px">')
        string = '<div style=\"width:20px;height:'+str(i*10)+'px;background:blue;border:1px solid red\"></div>'
        html.write(string)
        html.write('</td>')
    html.write('</tr>')
    html.write('<tr>')
    for i in groups:
        html.write('<td valign="bottom" style="width:25px">')
        string = '<p style="font-size:9px">'+i+'</p>'
        html.write(string)
        html.write('</td>')
    html.write('</tr>')
    html.write('</table>')
    html.write('</body></html>')



def main():
    data = open('input.txt')
    data = getSummary(data)
    writeHTML(data)

if __name__ == '__main__':
    main()
