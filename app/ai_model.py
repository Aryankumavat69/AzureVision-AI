from transformers import pipeline
from PIL import Image


print("Loading AI image analysis model...")

image_classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

print("AI model loaded successfully!")


def analyze_image(image_path: str):
    """
    Analyze an image and return the most likely
    visual categories with confidence scores.
    """

    image = Image.open(image_path).convert("RGB")

    predictions = image_classifier(image)

    results = []

    for prediction in predictions[:5]:
        results.append({
            "label": prediction["label"],
            "confidence": round(
                prediction["score"] * 100,
                2
            )
        })

    return results