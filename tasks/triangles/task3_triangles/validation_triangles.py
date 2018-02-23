def is_validation_count_data(data_triangle):
    return True if len(data_triangle) == 4 else False


def is_validation_value(data_triangle):
    return True if (data_triangle[0].isalnum()) and \
                   float(data_triangle[1]) > 0 and \
                   float(data_triangle[2]) > 0 and \
                   float(data_triangle[3]) > 0 else False


def is_triangle(first_side, second_side, third_side):
    return True if((first_side + second_side) > third_side) and \
            ((second_side + third_side) > first_side) and \
            ((third_side + first_side) > second_side) else False
