x_list = []
y_list = []
facing_list = []
direction_tuple = ('N', 'E', 'S', 'W')  # order of 90 degree rotation will never change
instructions_list = []
boundaries = []


# Reads each line of file and populates lists
def read_file(filepath):
    with open(filepath) as fp:
        line = fp.readline()
        count = 1

        while line:
            line_list = line.split()
            # First line sets max size
            if count == 1:
                [boundaries.append(i) for i in line_list] # Set boundaries
                print('boundaries: [{}, {}]\n'.format(boundaries[0], boundaries[1]))
            # Even number lines are position and direction
            elif count % 2 == 0:
                x_list.append(line_list[0])
                y_list.append(line_list[1])
                facing_list.append(line_list[2])
                print('start place: {} {} {}'.format(line_list[0], line_list[1], line_list[2]))
            # Odd number lines are a set of instructions
            else:
                instructions = ''.join(line_list)
                print("instructions: {}\n".format(instructions))
                instructions_list.append(instructions)

            line = fp.readline()
            count += 1


# Reads instructions and executes commands in order
def move_mower(x, y, facing, instructions):
    for instruction in instructions:

        if instruction == 'L':
            # Rotates left with directions_tuple[0] as reset index value since it's the first tuple value
            facing = rotate_mower(0, -1, -1, facing)

        elif instruction == 'R':
            # Rotates right with directions_tuple[3] as reset index value since it's the last tuple value
            facing = rotate_mower(3, 0, 1, facing)

        elif instruction == 'F':
            if facing == 'E':
                if x != boundaries[0]: # Check for x-boundary
                    x += 1
            elif facing == 'W':
                if x != 0: # Can't go below 0
                    x -= 1
            elif facing == 'N':
                if y != boundaries[1]: # Check for y-boundary
                    y += 1
            elif facing == 'S':
                if y != 0: # Can't go below 0
                    y -= 1
            else:
                print("error")
    # Returns final position of mower and direction
    return ' '.join([str(x), str(y), facing])


# Rotates mower based on input. Moves up or down one value in directions_tuple based on increment value.
def rotate_mower(last_index, first_index, increment_val, facing):
    count = 0

    for direction in direction_tuple:

        if direction == facing:
            # check for last value in tuple
            if count == last_index:
                # reset index value to beginning or end of tuple based on rotation direction
                facing = direction_tuple[first_index]
                break

            else:
                facing = direction_tuple[count + increment_val]
                break
        count += 1
    return facing


# Executes commands for number of values in instructions_list
def make_all_moves(x_list, y_list, facing_list, instructions_list):
    for i in range(len(instructions_list)):
        mower = move_mower(int(x_list[i]), int(y_list[i]), facing_list[i], instructions_list[i])
        print("Final position of mower #{}: ".format(i + 1))
        print(mower)


read_file('file.txt')
make_all_moves(x_list, y_list, facing_list, instructions_list)
