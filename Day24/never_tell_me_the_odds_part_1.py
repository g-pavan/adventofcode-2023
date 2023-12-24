def find_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def find_x(m1, m2, c1, c2):
    return (c2-c1)/(m1-m2)

def find_y_old(m1, m2, c1, c2):
    return (m1*c2 - m2*c1)/(m1-m2)

def find_y(m, x, c):
    return m*x + c

def find_c(y, m ,x):
    return y-m*x

def get_line_equations(coordinates, velocities):
    equations = []

    for i in range(len(coordinates)):
        x1 = coordinates[i][0]
        y1 = coordinates[i][1]
        x2 = x1 + velocities[i][0]
        y2 = y1 + velocities[i][1]

        m = find_slope(x1, y1, x2, y2)
        c = find_c(y1, m, x1)
        equations.append((x1, y1, m, c))

    return equations

def get_interseptcs(line_equations, ranges, velocities):
    range_min = ranges[0]
    range_max = ranges[1]
    ans = 0

    for i in range(len(line_equations)):
        for j in range(i+1, len(line_equations)):
            equation1 = line_equations[i]
            equation2 = line_equations[j]
            x1_vel = velocities[i][0]
            x2_vel = velocities[j][0]
            if(equation1[2] != equation2[2]):
                x_intercept = find_x(equation1[2], equation2[2], equation1[3], equation2[3])
                # y_intercept = find_y(equation1[2], equation2[2], equation1[3], equation2[3])
                y_intercept = find_y(equation1[2], x_intercept, equation1[3])

                x_valid = (x_intercept > equation1[0]) == ((equation1[0] + x1_vel) > equation1[0])
                y_valid = (x_intercept > equation2[0]) == ((equation2[0] + x2_vel) > equation2[0])

                if(range_min <= x_intercept <= range_max) and (range_min <= y_intercept <= range_max) and x_valid and y_valid:
                    # print("Intersected points: ", equation1, equation2, x_intercept, y_intercept)
                    ans += 1

    return ans

if __name__ == "__main__":

    coordinates = []
    velocities = []

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            cooridnate, velocity = line.split('@')
            coordinate = list(map(int, cooridnate.split(',')))
            velocity = list(map(int, velocity.split(',')))

            coordinates.append(coordinate)
            velocities.append(velocity)
    
    # print(coordinates, velocities)

    line_equations = get_line_equations(coordinates, velocities)
    # print("Equations: ", line_equations)

    ans = get_interseptcs(line_equations, [200000000000000, 400000000000000], velocities)

    print(ans)