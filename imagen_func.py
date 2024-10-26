from vertexai.preview.vision_models import ImageGenerationModel

generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

def generateImage_imagen(prompt:str):

    response = generation_model.generate_images(
    prompt=prompt,
)
    response.images[0].save("./imagenGenerated/image.jpg",True)
    return

def editImage_imagen(prompt:str):
    return