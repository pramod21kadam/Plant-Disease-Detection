from .base import *
# import cv2

class PredictionCtrl(MethodView):
    # @token_required
    def post(self):
        try:
            # get file
            file = request.files['predict_img']
            if file:
                boolean , result =  PredictServ().predict(imageFile = file)
                print(result)
                if boolean:
                    return successRes(msg='Prediction complete', key='result', value= str(result)), 200
                return failureRes(msg = f"{result}"), 500
            return failureRes(msg="File('predict_img') not found"), 404
        except Exception as error:
            return failureRes(f"{error}"), 500
