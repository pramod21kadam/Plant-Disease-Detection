from .base import *
class PredictionCtrl(MethodView):
    @token_required
    def post(self):
        try:
            return successRes(msg = "Got msg"), 200
        except Exception as error:
            return failureRes(f"{error}"), 500
