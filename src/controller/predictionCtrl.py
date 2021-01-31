from .base import *
class PredictionCtrl(MethodView):
    def post(self):
        try:
            # print(getData(request))
            return successRes(msg = "Got msg"), 200
        except Exception as error:
            return failureRes(f"{error}"), 500
    
    def get(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass