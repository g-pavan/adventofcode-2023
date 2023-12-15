def hash(string):
    value = 0
    i = 0

    while(i < len(string)):
        value += ord(string[i])
        value *= 17
        value %= 256

        i += 1
    
    return value

if __name__ == "__main__":

    ans = 0

    with open('input.txt', 'r') as f:
        given = list(f.readline().strip().split(','))

    for string in given:    
        ans += hash(string)
    
    print(ans)