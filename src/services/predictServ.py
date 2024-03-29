from typing import List
from .base import *

class PredictServ:
    """ 
        Service for perdiction perpose.
    """
    def predict(self, imageFile):
        try:
            target = 'temp/'
            # Save image to temperary folder
            filename = imageFile.filename
            path = "".join([target, filename])
            imageFile.save(path)

            # Generate image for prediction
            test_image = generate_image(filename=path)

            # predict image
            result = list(Model().predict(test_image, batch_size=1)[0])
            
            # Remove the saved file
            os.remove(os.getcwd()+ '/' + path)
            
            largest = result.index(max(result))
            return True, classes[largest]
        except Exception as error:
            return False, error