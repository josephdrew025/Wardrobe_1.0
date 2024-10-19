from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from deepface import DeepFace
import shutil
import os

app = FastAPI()

# Directory to save uploaded images
UPLOAD_DIRECTORY = "./uploaded_images"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

#face recognition
dfs = DeepFace.find(
    img_path = f"{UPLOAD_DIRECTORY}/unnamed.jpg",
    db_path = UPLOAD_DIRECTORY, 
    detector_backend = "retinaface",
    align = True
)
print(dfs)

# @app.post("/upload-image/")
# async def upload_image(file: UploadFile = File(...)):
    
#     # Define the file path where the image will be saved
#     file_location = f"{UPLOAD_DIRECTORY}/{file.filename}"
    
#     # Save the uploaded file to the upload directory
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
    
#     # Return the URI for accessing the image
#     # image_uri = f"http://localhost:8001/images/{file.filename}"

    
#     return JSONResponse(content={"matches": dfs})

# # Serve images from the upload directory
# @app.get("/images/{image_name}")
# async def get_image(image_name: str):
#     file_path = f"{UPLOAD_DIRECTORY}/{image_name}"
#     if os.path.exists(file_path):
#         return FileResponse(file_path)
#     return JSONResponse(content={"error": file_path}, status_code=404)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)
