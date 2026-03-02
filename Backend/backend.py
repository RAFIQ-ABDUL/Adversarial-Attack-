from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from fgsm import FGSM_Attack
from PIL import Image
import io
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = tf.keras.models.load_model("mnist_model.h5")
attack = FGSM_Attack(model)

@app.post("/attack")
async def run_attack(file: UploadFile = File(...), epsilon: float = 0.1):

    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("L")
    image = image.resize((28,28))

    img_array = np.array(image)/255.0
    img_array = img_array.reshape(1,28,28,1)

    clean_pred_tensor = tf.argmax(model(img_array), axis=1)
    clean_pred = int(clean_pred_tensor.numpy()[0])

    label_tensor = tf.convert_to_tensor([clean_pred])

    adv_img = attack.generate(img_array, label_tensor, epsilon)
    adv_pred = int(tf.argmax(model(adv_img), axis=1).numpy()[0])

    # Convert adversarial image to base64
    adv_img_np = adv_img.numpy()[0, :, :, 0] * 255
    adv_img_pil = Image.fromarray(adv_img_np.astype(np.uint8))

    buffered = io.BytesIO()
    adv_img_pil.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return {
        "clean_prediction": int(clean_pred),
        "adversarial_prediction": int(adv_pred),
        "attack_success": clean_pred != adv_pred,
        "adversarial_image": img_str
    }