import simple_operations as op

def service_blur(filename:str, kernel_size:int, id):
    op.save_image(op.apply_blur(filename, kernel_size), f'{id}.jpg')

def service_grayscale(filename:str, id):
    op.save_image(op.convert_to_gray(op.load_image(filename)), f'{id}.jpg')

def service_rotate(filename:str, angle:int, id):
    op.save_image(op.rotate_image(op.load_image(filename), angle), f'{id}.jpg')

def service_canny(filename:str, threshold1:int, threshold2:int, id):
    op.save_image(op.apply_canny(op.load_image(filename), threshold1, threshold2), f'{id}.jpg')


def service_convert_to_hsv(filename:str, id):
    # works, also breaks sometimes
    op.save_image(op.convert_to_hsv(op.load_image(filename)), f'{id}.jpg')

def service_flip_image(filename:str, direction:int, id):
    # works
    op.save_image(op.flip_image(op.load_image(filename), direction), f'{id}.jpg')

def service_apply_dilation(filename:str, kernel_size: int, iterations: int, id):
    # works
    op.save_image(op.apply_dilation(op.load_image(filename), kernel_size, iterations), f'{id}.jpg')

def service_apply_erosion(filename:str, kernel_size: int, iterations: int, id):
    # didn't test
    op.save_image(op.apply_erosion(op.load_image(filename), kernel_size, iterations), f'{id}.jpg')

def service_draw_contours(filename:str, contour_index:int, id):
    # works
    op.save_image(op.draw_contours(op.load_image(filename), contour_index), f'{id}.jpg')

def service_rotate_image(filename:str, angle:int, id):
    #works
    op.save_image(op.rotate_image(op.load_image(filename), angle), f'{id}.jpg')

def service_crop_image(filename:str, x:int, y:int, width:int, height:int, id):
    # works
    op.save_image(op.crop_image(op.load_image(filename), x, y, width, height), f'{id}.jpg')

def service_resize_image(filename:str, width:int, height:int, id):
    # works
    op.save_image(op.resize_image(op.load_image(filename), width, height), f'{id}.jpg')

def service_apply_median_blur(filename:str, kernel_size:int, id):
    # works
    op.save_image(op.median_blur(op.load_image(filename), kernel_size), f'{id}.jpg')

def service_apply_filter(filename:str, kernel, id):
    # works, needs another protocol to send the kernel
    op.save_image(op.apply_filter(op.load_image(filename), kernel), f'{id}.jpg')

def service_apply_sobel(filename:str, dx:int, dy:int, kernel_size:int, id):
    # works but i don't if the output is correct or not
    op.save_image(op.apply_sobel(op.load_image(filename), dx, dy, kernel_size), f'{id}.jpg')

def service_apply_shear(filename:str, shear_x:int, shear_y:int, id):
    # works
    op.save_image(op.apply_shear(op.load_image(filename), shear_x, shear_y), f'{id}.jpg')

def service_apply_affine_transformation(filename:str, transform_matrix, id):
    # works
    op.save_image(op.apply_affine_transformation(op.load_image(filename), transform_matrix), f'{id}.jpg')

def service_apply_perspective_transformation(filename:str, transform_matrix, id):
    # didn't test
    op.save_image(op.apply_perspective_transformation(op.load_image(filename), transform_matrix), f'{id}.jpg')

def service_equalize_histogram(filename:str, id):
    # works
    op.save_image(op.apply_histogram_equalization(op.load_image(filename)), f'{id}.jpg')

def service_find_and_draw_hough_lines(filename:str, rho, theta, threshold, id):
    # works but i don't know what the parameters do
    image = op.load_image(filename)
    op.save_image(op.draw_hough_lines(image, op.hough_lines(image, rho, theta, threshold)), f'{id}.jpg')

def service_apply_harris_corner_detection(filename:str, block_size:int, ksize:int, k:float, id):
    # works but i don't know what the parameters do
    op.save_image(op.apply_harris_corner_detection(op.load_image(filename), block_size, ksize, k), f'{id}.jpg')


# better error handling is needed i suppose XD