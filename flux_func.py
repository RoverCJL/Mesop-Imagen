import torch
from huggingface_hub import login
from dotenv import load_dotenv
from diffusers import FluxTransformer2DModel, FluxPipeline
from transformers import T5EncoderModel, CLIPTextModel
from optimum.quanto import freeze, qfloat8, quantize

load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')

login(access_token)

def generateImage_flux(prompt:str):
    text = prompt  # @param {type: "string"}
    height = 1024  # @param {type:"number"}
    width = 1024  # @param {type:"number"}
    num_inference_steps = 4  # @param {type:"number"}

    instances = [{"text": text}]
    parameters = {
        "height": height,
        "width": width,
        "num_inference_steps": num_inference_steps,
    }
    endpoint = aiplatform.Endpoint(FLUX_ENDPOINT_ID)
    # The default num inference steps is set to 4 in the serving container, but
    # you can change it to your own preference for image quality in the request.
    response = endpoint.predict(instances=instances, parameters=parameters)
    images = [
        base64_to_image(prediction.get("output")) for prediction in response.predictions
    ]

    # Create a file name
    output_file = f"./fluxGenerated/fluxImage.png"

    images[0].save(output_file)

    return
