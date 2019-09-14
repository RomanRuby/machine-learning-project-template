FROM ubuntu:18.04
MAINTAINER Roman Nagibov <roman.nagibov@gmail.com>

# Install build-essential, git, wget and other dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    libfreetype6-dev \
    libopenblas-dev \
    libopencv-dev \
    liblapack-dev \
    python \
    python-dev \
    python-pip \
    python-setuptools \
    python-numpy \
    graphviz \
    python-setuptools \
    wget \
    screen \
    rsync \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /tmp/.
WORKDIR /tmp
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6006 8888

WORKDIR "/root"
CMD ["/bin/bash"]
