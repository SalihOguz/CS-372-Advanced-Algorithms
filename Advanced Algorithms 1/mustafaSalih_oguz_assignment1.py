# mustafa salih oguz 213012263
def bag_switch (outcomes):
    first = ["B", "Y", "G"]
    if outcomes[0] not in first:
        return 0
    if outcomes[-1] in first:
        return None
    return bag_recursive(outcomes, 1)

def binary_search(outcomes, first, last):
    firstBag = ["B", "Y", "G"]
    if last - first <= 1:
        return last
    if outcomes[(last + first)/2] in firstBag:
        return binary_search(outcomes, (last + first)/2, last)
    else:
        return binary_search(outcomes, first, (last + first)/2)

def bag_recursive(outcomes, index):
    firstBag = ["B", "Y", "G"]
    try:
        lastItem = outcomes[index*2]
        last = index*2
    except:
        last = index+1
    if outcomes[index] in firstBag and outcomes[last] not in firstBag:
        return binary_search(outcomes, index, last)
    else:
        return bag_recursive(outcomes, index*2)

def partition_list(numbers):
    highIndex = len(numbers)-1
    lowIndex = 0
    peaked = False

    for i in range(len(numbers)):
        if numbers[i] >= numbers[lowIndex]:
            if peaked:
                break
            lowIndex = i
        else:
            peaked = True
            highIndex = i

    lowIndex = partition_min_recursive(numbers, min(numbers[lowIndex:highIndex]), 0)
    highIndex = partition_max_recursive(numbers, max(numbers[lowIndex:highIndex]), len(numbers)-1)

    return (lowIndex, highIndex)

def partition_min_recursive(numbers, min, index):
    if numbers[index] > min:
        return index
    else:
        return partition_min_recursive(numbers, min, index + 1)

def partition_max_recursive(numbers, max, index):
    if numbers[index] < max:
        return index
    else:
        return partition_max_recursive(numbers, max, index - 1)

def number_of_paths (G, start, end) :
    dic = {}
    for i, j in G:
        dic.setdefault(i, [])
        dic[i].append(j)
    return recursiveDFS(dic, [start], end, [], 0)

def recursiveDFS(dic, stack, end, visited, count):
    if len(stack) > 0:
        node = stack.pop()
        visited.append(node)
    else:
        return count
    for i in dic[node]:
        if i == end:
            count += 1
        elif i in dic.keys():
            stack.append(i)
    return recursiveDFS(dic, stack, end, visited, count)