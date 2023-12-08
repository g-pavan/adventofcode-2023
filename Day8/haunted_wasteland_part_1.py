def instruction_mapper(direction):
    if(direction == 'R'):
        return 1
    return 0

def haunted_wasteland(instructions, route_map):
    steps = 0
    curr_path = 'AAA'
    i = 0
    n = len(instructions)

    while(curr_path != 'ZZZ'):
        if(i == n):
            i = 0
        
        curr_path = route_map[curr_path][instructions[i]]
        i += 1
        steps += 1

    return steps



if __name__ == "__main__":

    instructions = ""
    route_map = {}

    with open("input.txt", "r") as f:
        line = f.readline()
        line.strip()

        instructions = line

        f.readline()

        while True:
            line = f.readline()
            if not line:
                break

            line = line.strip().split("=")
    
            line[-1] = line[-1].replace('(', '')
            line[-1] = line[-1].replace(')','')
            line[-1] = line[-1].replace(' ','')

            route_map[line[0].strip()] = tuple(line[-1].split(','))
    
    instructions = instructions.strip()
    instructions = list(map(instruction_mapper, instructions))
    # print(route_map)
        
    ans = haunted_wasteland(instructions, route_map)
    print(ans)