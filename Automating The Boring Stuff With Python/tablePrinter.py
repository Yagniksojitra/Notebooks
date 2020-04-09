def colWidths(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
    return colWidths



def printTable(tableData, colWidths):
    for i in range(len(tableData[0])): # i = 4 meaning the output has 4 rows
        #print (i)
        for j in range(len(tableData)): # j = 3 to output each row
            print (tableData[j][i].rjust(colWidths[j]), end=' ')
        print ()

        
        
if __name__ == '__main__':
    tableData = [['apples', 'Alice', 'dogs'],
              ['oranges', 'Bob', 'cats'],
              ['cherries', 'Carol', 'moose'],
              ['banana', 'David', 'goose']]
    colWidths = colWidths(tableData)
    printTable(tableData, colWidths)