from diffusers import AutoPipelineForText2Image 
import torch
import cv2

pipeline= AutoPipelineForText2Image.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype= torch.float16).to("cuda")
pipeline.load_lora_weights(r"C:\Users\PNP\Desktop\Nappi\ModelliLora\checkpoint-5000", weight_name="pytorch_lora_weights.safetensors")
image= pipeline("a woman in white dress").images[0]

im1=image.save("generazione.jpg")