#Alek Polesky 261068382

def is_valid_image(image_list):
    '''(list<list>) -> bool
     Takes a nested list as input, and returns True if the nested list represents a valid
    (non-compressed) PGM image matrix and False otherwise.
    >>> is_valid_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> is_valid_image([1, 3, 4, 5], [2, 3])
    False
    >>> is_valid_image(['lol'])
    False
    '''
    
    for i in range(len(image_list)):
        if len(image_list[i]) != len(image_list[0]):
            return False
        for j in range(len(image_list[i])):
            if type(image_list[i][j]) != int:
                return False
            elif image_list[i][j] < 0:
                return False
            elif image_list[i][j] > 255:
                return False
    
    return True

def is_valid_compressed_image(im_list):
    '''(list<list>) -> bool
    Takes a nested list as input and returns True if the matrix represents a valid
    compressed PGM image file. Returns False otherwise.
    >>> is_valid_compressed_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    >>> is_valid_compressed_image(['0x3', '71x5', 2x1'], ['240x9'])
    True
    >>> is_valid_compressed_image(['ZxB'])
    False
    '''
    first_b_value = 0
    current_b_value = 0
    
    #First check if 'x' in str
    #Idea: split str at x and check if A is an int between 0 and 255 and if B is an int
    
    for i in range(len(im_list)):
        if current_b_value != first_b_value:
            return False
        current_b_value = 0
        for j in range(len(im_list[i])):
            if type(im_list[i][j]) != str:
                return False
            if 'x' not in im_list[i][j]:
                return False
            a_value = im_list[i][j].split('x')[0]
            b_value = im_list[i][j].split('x')[1]
            if not a_value.isdigit():
                return False
            a_value = int(a_value)
            if int(a_value) < 0 or int(a_value) > 255:
                return False
            if not b_value.isdigit():
                return False
            b_value = int(b_value)
            if i == 0:
                first_b_value += b_value
                current_b_value += b_value
            else:
                current_b_value += b_value
                
    return True

def load_regular_image(filename):
    '''(str) -> list<list>
    Takes the string of a PGM file name as input and returns the image contained in the file as
    an image matrix. If the file is not in PGM format, an AssertionError is raised.
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> load_regular_image('mountain.pgm')
    [[187, 181, 171, 173, 173, 168, 168, 173, 178, 178, 174, 172, 169, 167, 167, 166, 167, 173, 178, 180, 178, 176, 184, 188, 182, 171, 168, 169, 175, 178, 177, 175, 176, 188, 207, 219, 223, 225, 232, 231, 224, 215, 205, 199, 195, 190, 190, 186, 177, 160, 143, 138, 135, 123, 114, 111, 106, 103, 102, 99, 95, 96, 102, 101, 100, 103, 106, 106, 109, 108, 107, 101, 92, 89, 87, 86, 87, 88, 88, 89, 91, 89, 89, 98, 106, 105, 102, 97, 91, 88, 84, 81, 80, 81, 84, 81, 78, 78, 77, 76, 76, 77, 78, 78, 78, 77, 78, 77, 79, 79, 83, 82, 82, 82, 82, 82, 81, 80, 78, 78, 78, 79, 79, 78, 78, 79, 79, 79, 80, 82, 88, 92, 89, 84, 81, 85, 86, 85, 83, 78, 79, 81, 77, 75, 76, 77, 74, 75, 76, 77, 79, 80, 81, 84, 86, 86, 85, 85, 88, 88, 84, 85, 87, 90, 91, 94, 98, 97, 95, 97, 104, 113, 119, 122, 133, 150, 157, 155, 157, 159, 159, 157, 149, 140, 134, 135, 132, 135, 142, 141, 136, 140, 145, 158, 171, 178, 186, 189, 191, 191, 196, 203, 207, 209, 205, 201, 194, 193, 191, 196, 199, 201, 206, 209, 206, 200, 194, 195, 191, 191, 192, 191, 195, 200, 201, 201, 202, 204, 211, 208, 203, 208, 215, 220, 225, 232, 237, 238, 237, 235, 238, 239, 237, 238, 233, 229, 228, 225, 223, 221, 217, 216, 219, 215, 210, 210, 218, 224, 226, 226, 225, 224, 226, 228, 229, 232, 230, 231, 232, 231, 229, 228, 228, 230, 233, 236, 239, 238, 240, 242, 244, 245, 246, 246, 246, 247, 247, 248, 247, 248, 249, 250, 250, 250, 249, 250, 251, 251, 251, 250, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 250, 250, 250, 250, 249, 249, 249, 249, 247, 245, 244, 243, 241, 235, 229, 227, 222, 215, 212, 210, 205, 201, 200, 195, 190, 187, 185, 184, 182, 181, 181, 176, 171, 169, 167, 167, 167, 168, 174, 176, 174, 176, 181, 177, 173, 168, 162, 158, 158, 160, 157, 156, 154, 150, 147, 145, 145, 142, 143, 143, 142, 138, 136, 132, 128, 131, 131, 130, 134, 141, 146, 149, 157, 165, 169, 173, 181, 188, 194, 198, 203, 210, 220, 228, 227, 226, 227, 230, 230, 232, 234, 235, 237, 239, 239, 241, 241, 244, 245, 246, 246, 247, 247, 247, 247, 249, 249, 249], [184, 182, 177, 176, 175, 174, 174, 176, 180, 179, 175, 172, 172, 170, 170, 170, 169, 173, 180, 184, 184, 185, 190, 193, 188, 177, 170, 168, 167, 166, 167, 168, 167, 182, 199, 215, 222, 221, 225, 228, 229, 223, 215, 205, 197, 195, 196, 193, 183, 168, 152, 142, 135, 127, 116, 114, 111, 109, 109, 107, 107, 108, 112, 111, 109, 111, 117, 120, 123, 118, 111, 101, 94, 91, 89, 87, 86, 89, 90, 89, 92, 91, 94, 99, 101, 106, 107, 102, 94, 88, 82, 79, 79, 79, 80, 81, 80, 78, 77, 78, 79, 79, 78, 77, 78, 78, 78, 79, 80, 82, 85, 88, 87, 86, 84, 83, 80, 79, 77, 78, 79, 79, 78, 76, 77, 77, 78, 78, 79, 81, 85, 90, 90, 87, 85, 87, 90, 88, 83, 79, 77, 77, 77, 76, 76, 77, 75, 74, 75, 76, 78, 78, 78, 81, 83, 83, 82, 84, 87, 85, 82, 83, 84, 87, 90, 94, 95, 94, 92, 94, 98, 103, 109, 115, 125, 138, 144, 144, 146, 152, 156, 157, 152, 143, 134, 132, 129, 131, 137, 136, 131, 129, 133, 144, 160, 174, 186, 190, 194, 195, 196, 202, 209, 213, 213, 207, 199, 196, 196, 197, 201, 204, 207, 211, 211, 204, 196, 194, 193, 193, 193, 191, 193, 201, 202, 201, 199, 198, 200, 202, 200, 205, 214, 219, 225, 234, 237, 240, 240, 240, 240, 241, 241, 242, 238, 235, 235, 234, 229, 223, 223, 223, 220, 221, 217, 214, 221, 225, 226, 229, 231, 228, 228, 233, 231, 233, 232, 231, 234, 232, 232, 232, 231, 232, 235, 237, 240, 241, 243, 244, 245, 247, 248, 246, 247, 247, 248, 249, 249, 250, 249, 249, 249, 250, 250, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251,…
    >>> load_regular_image('dragon.pgm')
    [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,…
    '''
    
    my_im_list = []
    i = 0
    fobj = open(filename, 'r')
    
    for line in fobj:
        if i < 3:
            i += 1
        else:
            new_line_list = []
            new_line = line.strip()
            new_line_list = new_line.split()
            for i in range(len(new_line_list)):
                if not new_line_list[i].isdigit():
                    raise AssertionError("There should only be numbers.")
                new_line_list[i] = int(new_line_list[i])
            my_im_list.append(new_line_list)
    fobj.close()
    
    if not is_valid_image(my_im_list):
        raise AssertionError('Not a valid regular PGM file type.')
    else:
        return my_im_list

def load_compressed_image(filename):
    '''(str) -> list<list>
    Takes a compressed image file name and returns an image matrix of
    the compressed image. If the file is not in PGM format, an assertion
    error is raised.
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> fobj = open("bad_test.pgm", "w")
    >>> fobj.write("P2C\\n30 5\\nINVALIDBAD\\nabc3x23 0x0x7\\n")
    >>> fobj.close()
    >>> load_compressed_image("invalid_test.pgm")
    Traceback (most recent call last):
    AssertionError: Not a valid compressed PGM file type.
    >>> fobj = open('another_ex.pgm', 'w')
    >>> fobj.write('P2C\\n30 1\\n240x30')
    17
    >>> fobj.close()
    >>> load_compressed_image('another_ex.pgm')
    []
    '''
    
    my_im_list = []
    i = 0
    fobj = open(filename, 'r')
    
    for line in fobj:
        if i < 3:
            i += 1
        else:
            new_line_list = []
            new_line = line.strip()
            new_line_list = new_line.split()
            my_im_list.append(new_line_list)
    fobj.close()
    
    if not is_valid_compressed_image(my_im_list):
        raise AssertionError('Not a valid compressed PGM file type.')
    else:
        return my_im_list

def load_image(filename):
    '''(str) -> list<list>
    Takes as a string the file name of a file as input. If the first line of the file is 'P2', then
    load_image loads the file as a regular PGM image matrix. If the first line is 'P2C', then the file
    is loaded as a compressed PGM image matrix. If the file is anything else, an AssertionError is raised.
    >>> load_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> load_image('dragon.pgm')
    [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,…
    >>> load_image('mountain.pgm')
    [[187, 181, 171, 173, 173, 168, 168, 173, 178, 178, 174, 172, 169, 167, 167, 166, 167, 173, 178, 180, 178, 176, 184, 188, 182, 171, 168, 169, 175, 178, 177, 175, 176, 188, 207, 219, 223, 225, 232, 231, 224, 215, 205, 199, 195, 190, 190, 186, 177, 160, 143, 138, 135, 123, 114, 111, 106, 103, 102, 99, 95, 96, 102, 101, 100, 103, 106, 106, 109, 108, 107, 101, 92, 89, 87, 86, 87, 88, 88, 89, 91, 89, 89, 98, 106, 105, 102, 97, 91, 88, 84, 81, 80, 81, 84, 81, 78, 78, 77, 76, 76, 77, 78, 78, 78, 77, 78, 77, 79, 79, 83, 82, 82, 82, 82, 82, 81, 80, 78, 78, 78, 79, 79, 78, 78, 79, 79, 79, 80, 82, 88, 92, 89, 84, 81, 85, 86, 85, 83, 78, 79, 81, 77, 75, 76, 77, 74, 75, 76, 77, 79, 80, 81, 84, 86, 86, 85, 85, 88, 88, 84, 85, 87, 90, 91, 94, 98, 97, 95, 97, 104, 113, 119, 122, 133, 150, 157, 155, 157, 159, 159, 157, 149, 140, 134, 135, 132, 135, 142, 141, 136, 140, 145, 158, 171, 178, 186, 189, 191, 191, 196, 203, 207, 209, 205, 201, 194, 193, 191, 196, 199, 201, 206, 209, 206, 200, 194, 195, 191, 191, 192, 191, 195, 200, 201, 201, 202, 204, 211, 208, 203, 208, 215, 220, 225, 232, 237, 238, 237, 235, 238, 239, 237, 238, 233, 229, 228, 225, 223, 221, 217, 216, 219, 215, 210, 210, 218, 224, 226, 226, 225, 224, 226, 228, 229, 232, 230, 231, 232, 231, 229, 228, 228, 230, 233, 236, 239, 238, 240, 242, 244, 245, 246, 246, 246, 247, 247, 248, 247, 248, 249, 250, 250, 250, 249, 250, 251, 251, 251, 250, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 250, 250, 250, 250, 249, 249, 249, 249, 247, 245, 244, 243, 241, 235, 229, 227, 222, 215, 212, 210, 205, 201, 200, 195, 190, 187, 185, 184, 182, 181, 181, 176, 171, 169, 167, 167, 167, 168, 174, 176, 174, 176, 181, 177, 173, 168, 162, 158, 158, 160, 157, 156, 154, 150, 147, 145, 145, 142, 143, 143, 142, 138, 136, 132, 128, 131, 131, 130, 134, 141, 146, 149, 157, 165, 169, 173, 181, 188, 194, 198, 203, 210, 220, 228, 227, 226, 227, 230, 230, 232, 234, 235, 237, 239, 239, 241, 241, 244, 245, 246, 246, 247, 247, 247, 247, 249, 249, 249], [184, 182, 177, 176, 175, 174, 174, 176, 180, 179, 175, 172, 172, 170, 170, 170, 169, 173, 180, 184, 184, 185, 190, 193, 188, 177, 170, 168, 167, 166, 167, 168, 167, 182, 199, 215, 222, 221, 225, 228, 229, 223, 215, 205, 197, 195, 196, 193, 183, 168, 152, 142, 135, 127, 116, 114, 111, 109, 109, 107, 107, 108, 112, 111, 109, 111, 117, 120, 123, 118, 111, 101, 94, 91, 89, 87, 86, 89, 90, 89, 92, 91, 94, 99, 101, 106, 107, 102, 94, 88, 82, 79, 79, 79, 80, 81, 80, 78, 77, 78, 79, 79, 78, 77, 78, 78, 78, 79, 80, 82, 85, 88, 87, 86, 84, 83, 80, 79, 77, 78, 79, 79, 78, 76, 77, 77, 78, 78, 79, 81, 85, 90, 90, 87, 85, 87, 90, 88, 83, 79, 77, 77, 77, 76, 76, 77, 75, 74, 75, 76, 78, 78, 78, 81, 83, 83, 82, 84, 87, 85, 82, 83, 84, 87, 90, 94, 95, 94, 92, 94, 98, 103, 109, 115, 125, 138, 144, 144, 146, 152, 156, 157, 152, 143, 134, 132, 129, 131, 137, 136, 131, 129, 133, 144, 160, 174, 186, 190, 194, 195, 196, 202, 209, 213, 213, 207, 199, 196, 196, 197, 201, 204, 207, 211, 211, 204, 196, 194, 193, 193, 193, 191, 193, 201, 202, 201, 199, 198, 200, 202, 200, 205, 214, 219, 225, 234, 237, 240, 240, 240, 240, 241, 241, 242, 238, 235, 235, 234, 229, 223, 223, 223, 220, 221, 217, 214, 221, 225, 226, 229, 231, 228, 228, 233, 231, 233, 232, 231, 234, 232, 232, 232, 231, 232, 235, 237, 240, 241, 243, 244, 245, 247, 248, 246, 247, 247, 248, 249, 249, 250, 249, 249, 249, 250, 250, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251, 251,…
    '''
    
    fobj = open(filename, 'r')
    for line in fobj:
        line = line.strip()
        if line == 'P2':
            fobj.close()
            return load_regular_image(filename)
        elif line == 'P2C':
            fobj.close()
            return load_compressed_image(filename)
        else:
            raise AssertionError('Not a valid PGM image file.')

def save_regular_image(im_list, filename):
    '''(list<list>, str) -> NoneType
    Takes a nested list and a filename (string) as input, and saves it in the PGM
    format to a file with the given file name. If the provided image matrix is not
    valid, an AssertionError is raised.
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0
    0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    >>> image = [['lol']]
    >>> save_regular_image(image, 'fail.pgm')
    Traceback (most recent call last):
    AssertionError: Not a valid regular PGM file type.
    >>> image = [[60]*5, [255]*5, [37]*5]
    >>> save_regular_image(image, "real.pgm")
    >>> image2 = load_image('real.pgm')
    >>> image == image2
    True
    '''
    if not is_valid_image(im_list):
        raise AssertionError('Not a valid regular PGM image file type!')
    
    height = len(im_list)
    width = len(im_list[0])
    
    fobj = open(filename, 'w')
    fobj.write('P2\n'+str(width)+' '+str(height)+'\n255\n')
    
    for i in range(len(im_list)):
        for j in range(len(im_list[i])):
            if j == len(im_list[i]) - 1:
                fobj.write(str(im_list[i][j])+'\n')
            else: 
                fobj.write(str(im_list[i][j])+' ')
    fobj.close()
    
def save_compressed_image(im_list, filename):
    ''' (list<list>, str) -> NoneType
    Takes a nested list and a file name's string as input, and saves it in the
    compressed PGM format to a file with the given file name. If the file is not
    in the compressed PGM image format, an AssertionError is raised.
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    >>> image = [['fail', 'lol']]
    >>> save_compressed_image(image, "fail.pgm")
    Traceback (most recent call last):
    AssertionError: Not a valid compressed PGM file type.
    >>> image = [["60x6", "201x4"], ["211x10"]]
    >>> save_compressed_image(image, "another_ex.pgm")
    >>> image2 = load_compressed_image("another_ex.pgm")
    >>> image == image2
    True
    '''
    if not is_valid_compressed_image(im_list):
        raise AssertionError('That\'s not a valid compressed PGM image file!')
    
    height = len(im_list)
    b_val_list = []
    
    for i in range(len(im_list[0])):
        b_val_list.append(int(im_list[0][i].split('x')[1]))
    
    width = sum(b_val_list)
    
    fobj = open(filename, 'w')
    fobj.write('P2C\n'+str(width)+' '+str(height)+'\n255\n')
    
    for i in range(len(im_list)):
        for j in range(len(im_list[i])):
            if j == len(im_list[i]) - 1:
                fobj.write(str(im_list[i][j])+'\n')
            else: 
                fobj.write(str(im_list[i][j])+' ')
    fobj.close()
    
def save_image(im_list, filename):
    ''' (list<list>, str) -> NoneType
    Takes a nested list and a file name (string as input) checks if the elements in im_list are integers
    or strings. If they are integers, im_list is saved as a regular PGM image file. If they are strings,
    im_list is saved as a compressed PGM image file. Raises an AssertionError if they are anything else.
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    >>> image = [['fail', 'lol']]
    >>> save_compressed_image(image, "fail.pgm")
    Traceback (most recent call last):
    AssertionError: Not a valid PGM file type.
    >>> image = [[60]*5, [255]*5, [37]*5]
    >>> save_regular_image(image, "real.pgm")
    >>> image2 = load_image('real.pgm')
    >>> image == image2
    True
    '''
    
    if type(im_list[0][0]) == int:
        save_regular_image(im_list, filename)
    elif type(im_list[0][0]) == str:
        save_compressed_image(im_list, filename)
    else:
        raise AssertionError('im_list must have either strings or ints')

def invert(im_list):
    '''(list<list>) -> list<list>
    Takes a regular PGM image matrix as input, and returns the inverted image.
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image = [[24, 35, 23, 7], [55, 31, 42, 6]]
    >>> invert(image)
    [[231, 220, 232, 248], [200, 224, 213, 249]]
    >>> image = [[470, 489719438, 198374]]
    >>> invert(image)
    Traceback (most recent call last):
    AssertionError: Not a valid regular PGM image matrix.
    '''
    
    if not is_valid_image(im_list):
        raise AssertionError('Not a valid regular PGM image matrix.')
    
    im_list_inverted = []
    for elmt in im_list:
        new_e = []
        for n in elmt:
            new_e.append(n)
        im_list_inverted.append(new_e)
    
    for i in range(len(im_list_inverted)):
        for j in range(len(im_list_inverted[i])):
            im_list_inverted[i][j] = abs(im_list_inverted[i][j] - 255)
    return im_list_inverted
    
def flip_horizontal(im_list):
    ''' (list<list>) -> list<list>
    Takes a regular PGM image matrix as input and returns
    the horizontally flipped version of the image matrix.
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    >>> image = [[24, 35, 23, 7], [55, 31, 42, 6]]
    >>> flip_horizontal(image)
    [[7, 23, 35, 24], [6, 42, 31, 55]]
    >>> image = [[470, 489719438, 198374]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: Not a valid regular PGM image matrix.
    '''
    
    if not is_valid_image(im_list):
        raise AssertionError('Not a valid regular PGM image matrix.')
 
    im_list_hflip = []
    for elmt in im_list:
        new_e = []
        for n in elmt:
            new_e.append(n)
        im_list_hflip.append(new_e)
     
    for i in range(len(im_list_hflip)):
        for j in range(len(im_list_hflip[i])//2):
            tmp = im_list_hflip[i][j]
            im_list_hflip[i][j] = im_list_hflip[i][len(im_list_hflip[i])-j-1]
            im_list_hflip[i][len(im_list_hflip[i])-j-1] = tmp
    
    return im_list_hflip

def flip_vertical(im_list):
    ''' (list<list>) -> list<list>
    Takes a regular PGM image matrix as input and returns
    the vertically flipped version of the image matrix.
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    >>> image = [[470, 489719438, 198374]]
    >>> flip_vertical(image)
    Traceback (most recent call last):
    AssertionError: Not a valid regular PGM image matrix.
    >>> image = [[24, 35, 23, 7], [55, 31, 42, 6]]
    >>> flip_vertical(image)
    [[55, 31, 42, 6], [24, 35, 23, 7]]
    '''
    
    if not is_valid_image(im_list):
        raise AssertionError('Not a valid regular PGM image matrix.')
    
    im_list_vflip = []
    for elmt in im_list:
        new_e = []
        for n in elmt:
            new_e.append(n)
        im_list_vflip.append(new_e)
        
    for i in range(len(im_list_vflip)//2):
        
        tmp = im_list_vflip[i]
        im_list_vflip[i] = im_list_vflip[len(im_list_vflip)-i-1]
        im_list_vflip[len(im_list_vflip)-i-1] = tmp
    
    return im_list_vflip
    
def crop(im_list, start_row, start_column, num_rows, num_columns):
    ''' (list<list>, int, int, int, int) -> list<list>
    Takes a regular PGM image matrix, and four ints as input. start_row and start_column represent
    the starting position of the rectangle, and num_rows and num_columns specify how large the
    target rectangle should be.
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    >>> crop([[6, 7], [5, 7, 8]], 1, 1, 1, 1)
    Traceback (most recent call last):
    AssertionError: Not a valid regular PGM image matrix
    >>> crop([[55, 9, 4], [2, 41, 11], [224, 6, 88]], 0, 0, 2, 2)
    [[55, 9], [2, 41]]
    '''
    
    if not is_valid_image(im_list):
        raise AssertionError('Not a valid regular PGM image matrix.')
    
    im_list_copy = []
    for elmt in im_list:
        new_e = []
        for n in elmt:
            new_e.append(n)
        im_list_copy.append(new_e)
    
    im_list_crop = []
    empty_list = []
    current_row = []
    for i in range(start_row, start_row + num_rows):
        if current_row != empty_list:
            im_list_crop.append(current_row[:])
        current_row = []
        for j in range(start_column, start_column + num_columns):
            current_row.append(im_list_copy[i][j])
    
    im_list_crop.append(current_row[:])
    
    return im_list_crop
    
def find_end_of_repetition(int_list, index, target):
    ''' (list<int>, int, int) -> int
    Takes a list of ints, index, and target as input and looks through the list starting after
    the given index, and returns the index of the last consecutive occurrence of the target number.
    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4
    >>> find_end_of_repetition([6, 6, 6, 6, 7], 0, 6)
    3
    >>> find_end_of_repetition([6, 8, 6, 6, 7], 0, 6)
    0
    '''
    
    if index == len(int_list) - 1:
        return len(int_list) - 1
    for i in range(index, len(int_list)):
        if int_list[i] != target:
            return i - 1
    return len(int_list) - 1

def compress(im_list):
    ''' (list<list>) -> list<list>
    Takes a regular PGM image matrix and compresses it according to
    the compression algorithm descirbed in the PDF.
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    >>> compress([[12, 12, 12, 1, 1,], [7, 7, 8, 8, 0]])
    [['12x3', '1x2'], ['7x2', '8x2', '0x1']]
    >>> compress([['lol'], ['invalid']])
    Traceback (most recent call last):
    AssertionError: Not a valid regular PGM image matrix.
    '''
    
    if not is_valid_image(im_list):
        raise AssertionError('Not a valid regular PGM image matrix.')

    compressed_list = []
    current_row = []
    for i in range(len(im_list)):
        if current_row != []:
            compressed_list.append(current_row[:])
            current_row = []
        j = 0
        while j < len(im_list[i]):
            a_value = im_list[i][j]
            b_value = 0
            for k in range(j, len(im_list[i])):
                if im_list[i][k] == im_list[i][j]:
                    b_value += 1
                else:
                    break
            current_row.append(str(a_value)+'x'+str(b_value))
            if find_end_of_repetition(im_list[i], j, im_list[i][j]) == 0:
                j += 1
            else:
                j = find_end_of_repetition(im_list[i], j, im_list[i][j]) + 1
    
    compressed_list.append(current_row[:])
           
    
    return compressed_list

def decompress(im_list):
    '''(list<list>) -> list<list>
    Takes a compressed PGM image matrix as input and decompresses it according to the
    compression algorithm described in the assignment PDF.
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> decompress([['12x7'], ['2x5', '3x2']])
    [[12, 12, 12, 12, 12, 12, 12], [2, 2, 2, 2, 2, 3, 3]]
    >>> decompress([['this is not valid']])
    Traceback (most recent call last):
    AssertionError: That's not a valid compressed PGM image matrix!
    '''
    
    if not is_valid_compressed_image(im_list):
        raise AssertionError('That\'s not a valid compressed PGM image matrix!')
    
    current_row = []
    decompressed_list = []
    for i in range(len(im_list)):
        if current_row != []:
            decompressed_list.append(current_row[:])
        current_row = []
        for j in range(len(im_list[i])):
            a_value = im_list[i][j].split('x')[0]
            b_value = im_list[i][j].split('x')[1]
            for k in range(int(b_value)):
                current_row.append(int(a_value))
    
    decompressed_list.append(current_row[:])
    
    return decompressed_list
    
def process_command(commands):
    ''' (str) -> NoneType
    Takes a string as input corresponding to a series of space-separated image processing
    commands, and executes each command in order. Returns nothing.
    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    True
    >>> process_command('LOAD<comp.pgm> do something')
    Traceback (most recent call last):
    AssertionError: One or more of your commands are not valid.
    >>> process_command("LOAD<comp.pgm> INV FH FV CP SAVE<another_ex.pgm>")
    >>> load_image('another_ex.pgm')
    [['255x24'], ['255x4', '0x1', '255x1', '68x1', '255x1', '68x1', '255x1', '68x1', '255x1', '136x5', '255x1', '204x5', '255x1'], ['255x4', '0x1', '255x1', '68x1', '255x1', '68x1', '255x1', '68x1', '255x1', '136x1', '255x3', '136x1', '255x5', '204x1', '255x1'], ['255x1', '0x4', '255x1', '68x1', '255x1', '68x1', '255x1', '68x1', '255x1', '136x1', '255x3', '136x1', '255x5', '204x1', '255x1'], ['255x1', '0x1', '255x2', '0x1', '255x1', '68x1', '255x1', '68x1', '255x1', '68x1', '255x1', '136x1', '255x3', '136x1', '255x5', '204x1', '255x1'], ['255x1', '0x4', '255x1', '68x5', '255x1', '136x5', '255x1', '204x5', '255x1'], ['255x24']]
    '''
    
    command_list = commands.split()
    
    for command in command_list:
        if 'LOAD' in command:
            filename = command.split('<')[1].strip('>')
            im_list = load_image(filename)
        elif 'SAVE' in command:
            filename = command.split('<')[1].strip('>')
            save_image(im_list, filename)
        elif command == 'INV':
            im_list = invert(im_list)
        elif command == 'FH':
            im_list = flip_horizontal(im_list)
        elif command == 'FV':
            im_list = flip_vertical(im_list)
        elif 'CR' in command:
            nums = command.split('<')[1].strip('>')
            nums_list = nums.split(',')
            y = nums_list[0]
            x = nums_list[1]
            h = nums_list[2]
            w = nums_list[3]
            
            im_list = crop(im_list, y, x, h, w)
            
        elif command == 'CP':
            im_list = compress(im_list)
        elif command == 'DC':
            im_list = decompress(im_list)
        else:
            raise AssertionError("One or more of your commands are not valid.")
            