FROM tensorflow/tensorflow:1.12.0-gpu-py3

# installation instructions from http://nlp_architect.nervanasys.com/installation.html

RUN apt-get update && apt-get install -y \
    git \
    libhdf5-dev \
    locales \
    pkg-config \
    wget

# fix python encode/decode error in Ubuntu
# from https://stackoverflow.com/questions/27931668/encoding-problems-when-running-an-app-in-docker-python-java-ruby-with-u/27931669
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /tmp

# use Anaconda instead of virtualenv to manage virtual environments
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN /opt/conda/bin/conda create -y -n nlp-architect setuptools wheel jupyter python=3.6

WORKDIR /opt

RUN export NLP_ARCHITECT_BE=GPU && \
    git clone https://github.com/NervanaSystems/nlp-architect.git && \
    cd nlp-architect && \
    # since it is not recommended to have build time GPU support, we will modify requirements.txt to explicitly install
    # tensorflow-gpu.
    # see: https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#can-i-use-the-gpu-during-a-container-build-ie-docker-build
    sed -i 's/tensorflow==/tensorflow-gpu==/' requirements.txt && \
    /opt/conda/envs/nlp-architect/bin/pip install -e .

# expose port for jupyter
EXPOSE 8888
# expose port for bokeh server
EXPOSE 5006
CMD /opt/conda/envs/nlp-architect/bin/jupyter notebook --notebook-dir=/opt/nlp-architect --ip 0.0.0.0 --no-browser --allow-root