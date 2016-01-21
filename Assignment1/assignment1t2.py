#-------------------------------------------------------------------------------
# Name:        Task 2
# Purpose:
#
# Author:      Zhao
#
# Created:     11/01/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getInfo(file):
    return_List = []
    index = 1
    for i in file.readlines():
        element = []
        i = i.split(';')
        for j in i:
            if j.find('\n')>0:
               j = j[:j.find('\n')]    # Eliminating \n
            if j.find('.') != -1:   # change 'rate' from str to float
               j = float(j)
            elif len(j) <= 4:       # change 'calling_duration from str to int
                 j = int(j)
            element.append(j)
        if len(element) < 5:
           element.insert(0,str(index))
           element.append(0)
        index += 1
        return_List.append(element)
    return return_List

def getkey(a):
    return a[1]

def summarizeInfoForNodes(calls, nodes, directed, edgeWeight):
    dic = {}
    for i in nodes:
        for j in nodes:
            if i[0] != j[0]:
               dic[i[0]+ ', '+j[0]] = 0
    for call in calls:
        for node in nodes:
            if directed == '1' and edgeWeight == '0':
               if call[1] == node[1]:
                  node[4] += call[3]
            if directed == '1' and edgeWeight == '1':
               if call[1] == node[1]:
                  node[4] += 1
            if directed == '0' and edgeWeight == '0':
               if call[1] == node[1] or call[2] == node[1]:
                  node[4] += call[3]
            if directed == '0' and edgeWeight == '1':
               if call[1] == node[1] or call[2] == node[1]:
                  node[4] += 1
            for edge in nodes:
                if directed == '1' and edgeWeight == '0':
                   if call[1] == node[1] and call[2] == edge[1]:
                      dic[node[0]+ ', ' +edge[0]] += call[3]
                elif directed == '1' and edgeWeight =='1':
                     if call[1] == node[1] and call[2] == edge[1]:
                        dic[node[0]+ ', ' +edge[0]] += 1
                elif directed == '0' and edgeWeight =='0':
                     if (call[1] == node[1] and call[2] == edge[1]) or (call[2] == node[1] and call[1] == edge[1]):
                        dic[node[0]+ ', ' +edge[0]] += call[3]
                elif directed == '0' and edgeWeight =='1':
                     if (call[1] == node[1] and call[2] == edge[1]) or (call[2] == node[1] and call[1] == edge[1]):
                        dic[node[0]+ ', ' +edge[0]] += 1
    return nodes, dic

def printFile(nodes, edges):
    file = open('callgraph.txt', 'w')
    for node in nodes:
        file.write(node[0]+', '+node[1]+', '+node[2]+', '+node[3] +', '+str(node[4]) +'\n')
    file.write('\n')
    for i in nodes:
        for j in nodes:
            if i[0] != j[0]:
               file.write(i[0]+', '+j[0]+ ', ' + str(edges[i[0]+', '+j[0]]) + '\n')


def main():
    customerFile = open('customers.txt')
    nodes = getInfo(customerFile)                       #[token, phoneNumber, Name, City, (numberOfCall, timeSpent)]
    sorted_nodes = sorted(nodes, key = getkey)
    customerFile.close()

    callsFile = open('calls.txt')
    calls = getInfo(callsFile)                          #[timeStamp, callerNo, reciverNo, time, rate]
    callsFile.close()

    directed = input('Date for:\nDirected graph .....1\nUndirected graph ...0')
    while str(directed) != '0' and str(directed) != '1':
       print('Please enter a number between 0 to 1')
       directed = input('Date for:\nDirected graph .....1\nUndirected graph ...0')

    edgeWeight = input('Edge weight is:\nThe number of calls ...1\nThe time spent .........0')
    while str(edgeWeight) != '0' and str(edgeWeight) != '1':
       print('Please enter a number between 0 to 1')
       edgeWeight = input('Edge weight is:\nThe number of calls ...1\nThe time spent .........0')
       
    summary = summarizeInfoForNodes(calls,sorted_nodes, directed, edgeWeight)
    summary_nodes = summary[0]
    summary_edges = summary[1]

    printFile(summary_nodes, summary_edges)
    for i in sorted_nodes:
        for j in sorted_nodes:
            if i[0] != j[0]:
               print(i[0]+', '+j[0]+ ', ' + str(summary_edges[i[0]+', '+j[0]]))


if __name__ == '__main__':
    main()
