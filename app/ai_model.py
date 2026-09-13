from PIL import Image
import onnxruntime as ort
import numpy as np
import json
import os


print("Loading lightweight MobileNetV2 ONNX model...")


MODEL_DIR = "models/mobilenet"


MODEL_PATH = os.path.join(
    MODEL_DIR,
    "model.onnx"
)


CONFIG_PATH = os.path.join(
    MODEL_DIR,
    "config.json"
)


# Load ONNX model
session = ort.InferenceSession(
    MODEL_PATH,
    providers=["CPUExecutionProvider"]
)


# Load labels
with open(
    CONFIG_PATH,
    "r",
    encoding="utf-8"
) as file:
    config = json.load(file)


id2label = {
    int(key): value
    for key, value in config["id2label"].items()
}


# Get model input information
input_info = session.get_inputs()[0]

input_name = input_info.name
input_shape = input_info.shape


print("ONNX input:", input_name)
print("ONNX input shape:", input_shape)

print("MobileNetV2 ONNX model loaded successfully!")


def preprocess_image(image_path: str):
    """
    Prepare an image for MobileNetV2.
    """

    image = Image.open(
        image_path
    ).convert("RGB")


    # Resize to model input size
    image = image.resize(
        (224, 224)
    )


    # Convert to NumPy
    image_array = np.asarray(
        image,
        dtype=np.float32
    )


    # Scale from [0, 255] to [0, 1]
    image_array = (
        image_array / 255.0
    )


    # ImageNet normalization
    mean = np.array(
        [0.485, 0.456, 0.406],
        dtype=np.float32
    )


    std = np.array(
        [0.229, 0.224, 0.225],
        dtype=np.float32
    )


    image_array = (
        image_array - mean
    ) / std


    # HWC → CHW
    image_array = np.transpose(
        image_array,
        (2, 0, 1)
    )


    # Add batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )


    return image_array.astype(
        np.float32
    )


def analyze_image(image_path: str):
    """
    Analyze an image and return the
    top 5 predictions.
    """

    inputs = preprocess_image(
        image_path
    )


    outputs = session.run(
        None,
        {
            input_name: inputs
        }
    )


    logits = np.asarray(
        outputs[0]
    )


    # Convert logits to probabilities
    exp_logits = np.exp(
        logits
        - np.max(
            logits,
            axis=-1,
            keepdims=True
        )
    )


    probabilities = (
        exp_logits
        / np.sum(
            exp_logits,
            axis=-1,
            keepdims=True
        )
    )


    # Get top 5 classes
    top_indices = np.argsort(
        probabilities[0]
    )[-5:][::-1]


    results = []


    for index in top_indices:

        label = id2label.get(
            int(index),
            f"Class {index}"
        )


        confidence = (
            probabilities[0][index]
            * 100
        )


        results.append({
            "label": label,
            "confidence": round(
                float(confidence),
                2
            )
        })


    return results