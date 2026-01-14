GOAL:
This project aims to generate image with AI for adversting purposes.
The goal is to generate images of models wearing a bag to be endorsed from a 360-degree video of the bag called "borsa.mp4".
To do this, we developed a LoRA model capable of recognizing and faithfully reproducing the bag.

PROCESS:
We used two python scripts to create the database:
1. The script called "Frame_from_video.py" automatically extracts frames at regular intervals from the source video, thus generating a set of images representing the Dataset.
2. The script called "Remove_background.py" removes the background from the frames so that the focus is exclusively on the bag.

We then use the open source Kohya_ss platform to develop the LoRA model that recognizes our bag.
Once the model is developed we use it on Stable diffusion installed locally to generate our images (unfortunately I lost the file .safetensors).

RESULTS:
I uploaded the images generated in different advertising contexts into the results folder.
