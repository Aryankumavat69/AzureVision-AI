from PIL import Image
from transformers import AutoImageProcessor
from optimum.onnxruntime import ORTModelForImageClassification
import numpy as np


print("Loading lightweight ONNX image analysis model...")


MODEL_ID = "google/vit-base-patch16-224"


processor = AutoImageProcessor.from_pretrained(
    MODEL_ID
)


model = ORTModelForImageClassification.from_pretrained(
    MODEL_ID,
    export=True
)


print("ONNX AI model loaded successfully!")


def analyze_image(image_path: str):
    """
    Analyze an image and return the top 5
    visual categories with confidence scores.
    """

    image = Image.open(
        image_path
    ).convert("RGB")


    inputs = processor(
        images=image,
        return_tensors="np"
    )


    outputs = model(
        **inputs
    )


    logits = np.asarray(
        outputs.logits
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


    # Get indexes of top 5 predictions
    top_indices = np.argsort(
        probabilities[0]
    )[-5:][::-1]


    results = []


    for index in top_indices:

        label = model.config.id2label[
            int(index)
        ]


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