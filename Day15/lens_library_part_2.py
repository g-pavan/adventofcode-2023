def hash(string):
    value = 0
    i = 0

    while(i < len(string)):
        value += ord(string[i])
        value *= 17
        value %= 256

        i += 1
    
    return value


def focusing_power(given):
    hashed_array = [[] for _ in range(256)]
    find_index = lambda lst, val: next((index for index, sublist in enumerate(lst) if sublist[0] == val), -1)


    ans = 0

    for string in given:
        if string[-1] == '-':
            data = string[:-1]
            hash_value = hash(data)
            ind = find_index(hashed_array[hash_value], data)
            if(ind != -1):
                hashed_array[hash_value].pop(ind)
        else:
            left, right = string.split('=')
            focal_length = int(right)
            hash_value = hash(left)
            
            ind = find_index(hashed_array[hash_value], left)

            if(ind != -1):
                hashed_array[hash_value][ind][1] = focal_length
            else:
                hashed_array[hash_value].append([left, focal_length])
        
        # print(hashed_array[:4])
    
    for i in range(len(hashed_array)):
        for j in range(len(hashed_array[i])):
            ans += ((i+1)*(j+1)*(hashed_array[i][j][1]))
    
    # print(hashed_array)
    return ans

if __name__ == "__main__":

    ans = 0

    with open('input.txt', 'r') as f:
        given = list(f.readline().strip().split(','))

    print(focusing_power(given))