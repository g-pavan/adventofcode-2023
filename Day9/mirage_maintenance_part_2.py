def mirage_maintenance(history):
    if(history.count(0) == len(history)):
        return 0
    
    diff = []

    i = 1

    while(i < len(history)):
        diff.append(history[i] -history[i-1])
        i += 1
    
    return history[0] - mirage_maintenance(diff)

if __name__ == "__main__":

    ans = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            history = (list(map(int, line.split())))
            k = mirage_maintenance(history)
            # print(k)
            ans += k
    
    print(ans)