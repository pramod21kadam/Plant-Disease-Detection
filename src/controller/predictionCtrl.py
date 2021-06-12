from numpy import delete
from .base import *
import requests

from database.database import Database

api_url = "http://127.0.0.1:5000/api/validate-token"


class PredictionCtrl(MethodView):
    # @token_required
    def post(self):
        try:
            # get file
            token = request.cookies.get("x-access-token")
            if token:
                data = {"x-access-token": token}
                response = requests.post(api_url, data)
                if (
                    response.status_code != 200
                    or response.json()["status"] != "success"
                ):
                    return response.json(), 400
            else:
                return failureRes(msg="invalid access"), 400

            file = request.files["predict_img"]
            if file:
                boolean, result = PredictServ().predict(imageFile=file)
                if boolean:
                    mongo = Database.getinstance().mongo
                    result = mongo.db.DiseaseInfo.find_one({"id": str(result)})

                    if not result:
                        return failureRes(msg="Failed to fetch result"), 500

                    result.pop("_id")
                    return (
                        successRes(
                            msg="Prediction complete", key="result", value=result
                        ),
                        200,
                    )
                return failureRes(msg=f"{result}"), 500
            return failureRes(msg="File('predict_img') not found"), 404
        except Exception as error:
            return failureRes(f"{error}"), 500
