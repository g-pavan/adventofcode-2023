def seed_to_location(seeds, start, destination, offset):

    for i in range(len(seeds)):
        j = 0
        while(j < len(start)):
            if(start[j] <= seeds[i]) and (seeds[i] < (start[j] + offset[j])):
                seeds[i] = (destination[j] + (seeds[i] - start[j]))
                break
            j += 1
    

if __name__ == "__main__":

    i = 0
    
    with open("input.txt", "r") as f:
        
        line = f.readline()
        seeds = list(map(int, line.split(":")[-1].split()))

        while True:
            line = f.readline()
            if not line:
                break  
            line = line.strip()

            if(len(line) != 0 and line[0].isdigit()):
                start = []
                destination = []
                offset = []

                while True:
                    
                    line = line.strip()
                    
                    if(len(line) == 0):
                        break
                    
                    values = list(map(int, line.strip().split()))

                    start.append(values[1])
                    destination.append(values[0])
                    offset.append(values[2])

                    line = f.readline()
                    if not line :
                        break  

                seed_to_location(seeds, start, destination, offset)
            
        
        print(min(seeds))