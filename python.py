# solution
def BFSListPath(AList, v, preventionList=[]):
    visited, parent = {}, {}
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    q = []

    visited[v] = True
    q.append(v)

    while len(q) > 0:
        j = q.pop(0)
        for k in AList[j]:
            if not visited[k] and not k in preventionList:
                visited[k] = True
                parent[k] = j
                q.append(k)
    return visited, parent

#Code
def findpath(parent, start, end):
    print('Two', parent, start, end)
    L = []
    curr = parent[end]
    while curr != start:
        L.append(curr)
        curr = parent[curr]
        print('l', L)
    return L

#Code
def backandforth(AList, start, end):
    preventionList = []
    visited, parent = BFSListPath(AList, start, preventionList)
    print('vs', visited, 'pa', parent)
    c = 0
    while visited[end]:
        c += 1
        path = findpath(parent, start, end)
        print(parent, start, end)
        print('path', path)
        preventionList.extend(path)
        print('pl', preventionList, 'vs', visited)
        visited, parent = BFSListPath(AList, start, preventionList)
        print('vs', visited, 'pa', parent)
    return c


# suffix (invisible)
start = int(input())
end = int(input())
AList = {}
while True:
    line = input()
    if line.strip() == '':
        break
    u, vs = line.strip().split(':')
    u = int(u)
    AList[u] = []
    for v in vs.strip().split():
        v = int(v)
        if v not in AList:
            AList[v] = []
        AList[u].append(v)
print(backandforth(AList, start, end))
