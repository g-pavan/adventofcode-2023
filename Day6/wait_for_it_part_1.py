def wait_for_it(time, distance):
    no_of_ways = 1
    start = 1
    end = time//2

    while(start <= end):
        mid = (start + end )//2
        speed = (time-mid)*mid

        if(speed > distance):
            no_of_ways = time - (mid - 1)*2 - 1
            end = mid - 1
        else:
            start = mid + 1
    
    return no_of_ways
        


if __name__ == "__main__":

    ans = 1

    with open("input.txt", "r") as f:
        line = f.readline()
        times = list(map(int, line.strip().split(":")[-1].split()))

        line = f.readline()
        distances = list(map(int, line.strip().split(":")[-1].split()))

    for i in range(len(times)):
        waits = wait_for_it(times[i], distances[i])
        ans *= waits

    print(ans)