# Introduction
This repository contains a script to generate a Dockerfile that contains Intel's [NLP Architect](https://github.com/NervanaSystems/nlp-architect)
with the option for CPU or GPU backend. Running the image will start a Jupyter server which
you can use to explore the library's repository.

# Requirements
This script requires Python 3.6 or above.

# Usage

## Create the Dockerfile
1. Clone this repository and navigate to the root folder.
2. Execute:
    ```
    python create_nlp_architect_dockerfile.py --backend=gpu
    ```
    to create an NLP Architect Dockerfile with a gpu backend (replace `gpu` with `cpu` if you
    want a cpu backend). Note the location of the Dockerfile.
    
## Run the image
Following the example in the previous section, execute the following command after you 
have built the image with `docker build` (assuming you tagged the image as `nlp_architect`):
```
docker run --runtime=nvidia -it -p 8888:8888 -p 5006:5006 nlp_architect
```
You can now open your web browser and navigate to your machine's ip address at port 8888 to
explore the NLP Architect repository. The `examples` and `tutorials` folder are a good
place to start.

Note: You will need [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) installed if you
plan on running the gpu version of the image.

# Contributions
Feel free to raise a pull request if you have any questions, feedback or contributions to share.
