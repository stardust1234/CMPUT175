#-------------------------------------------------------------------------------
# Name:        Read Webpage Elements
# Purpose:
#
# Author:      yizhou
#
# Created:     10/01/2016
# Copyright:   (c) yizhou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib.request

def gethtml(page):
    htmls = []
    for i in page:
        i = str(i)
        if i.count('href=')!=0:
           htmls.append(i)
    return htmls

def clean_element(useful_element):
    cleaned_element = []
    for i in useful_element:
        if i[i.find('>')+1] != '<':
           cleaned_element.append(i)
    return cleaned_element

def buildDic(cleaned_element):
    dictionary = {}
    for i in cleaned_element:
        i = i.split("\"")
        html = i[1]
        text = i[2][1:i[2].find('<')]
        dictionary[text] = html
    return dictionary


def main():
    html = urllib.request.urlopen('http://cs.ualberta.ca/')
    page = html.readlines()
    useful_element = gethtml(page)
    cleaned_element = clean_element(useful_element)
    dictionary = buildDic(cleaned_element)
    print(dictionary.keys())


main()