import requests
from database.database import Database

from .base import *

api_url = "http://127.0.0.1:5000/api/validate-token"


class PredictionCtrl(MethodView):
    """
    Perdiction contoller processes post requests only.
    Uses tensorflow model to classify image and returns the result fetched from database.
    """

    def post(self):
        try:
            # get file
            token = request.cookies.get("x-access-token")
            # check if user is signed in or not by vlaidating jwt token
            if token:
                # if token is present then send token to token validation api,
                data = {"x-access-token": token}
                response = requests.post(api_url, data)
                if (
                    response.status_code != 200
                    or response.json()["status"] != "success"
                ):
                    # invalid token
                    return response.json(), 400
            else:
                # token was not present in request hence don't prcess the request.
                return failureRes(msg="invalid access"), 400

            file = request.files["predict_img"]  # image file to be classified
            if file:
                # if file is present classify it.
                boolean, result = PredictServ().predict(imageFile=file)
                if boolean:
                    # if classification was successful fetch more information form database.
                    mongo = Database.getinstance().mongo
                    result = mongo.db.DiseaseInfo.find_one({"id": str(result)})

                    if not result:
                        # failed to fetch information form database
                        return failureRes(msg="Failed to fetch result"), 500

                    result.pop("_id")  # user don't need to see this better remove it.
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
