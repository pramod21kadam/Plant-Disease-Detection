from packages.packages import *
from utils.auth import check_for_token, generate_token, get_current_user
from dao.__init__ import *
from mobile_net.__init__ import Model
from utils.utils import classes
def generate_image(filename,img_width = 224, img_height=224):
    test_image = image.load_img(filename, target_size=(img_width, img_height))
    test_image = image.img_to_array(test_image)
    test_image = test_image/255.
    test_image = np.expand_dims(test_image, axis=0)
    return test_image