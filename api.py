import os
import uuid

from fastapi import FastAPI, File, UploadFile

from predictor import DepthEstimationModel

ALLOWED_EXTENSION = {".jpg", ".jpeg", ".png"}
TEMP_FOLDER = "api_images"
os.makedirs(TEMP_FOLDER, exist_ok=True)

app = FastAPI()
depth_estimator = DepthEstimationModel()


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        file_ext = os.path.splitext(file.filename)[1]
        if file_ext not in ALLOWED_EXTENSION:
            return {"error": "Uploaded file must be in JPG, JPEG or PNG format."}

        filename_base = str(uuid.uuid4())
        filename = filename_base + file_ext
        destination_path = os.path.join(TEMP_FOLDER, filename)
        output_path = os.path.join(TEMP_FOLDER, "output_" + filename_base + ".png")

        with open(destination_path, "wb") as image_data:
            image_data.write(file.file.read())

        depth_estimator.calculate_depth_map(destination_path, output_path)

    except Exception as e:
        return {"error": str(e)}