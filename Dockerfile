# Base image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_SDK_ROOT=/root/Android/Sdk
ENV PATH=$PATH:/root/Android/Sdk/tools:/root/Android/Sdk/platform-tools

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    openjdk-11-jdk \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libc6 \
    libc++1 \
    xvfb \
    x11-apps \
    nano \
    git \
    && apt-get clean

# Install Android Studio
RUN wget https://redirector.gvt1.com/edgedl/android/studio/ide-zips/2022.3.1.20/android-studio-2022.3.1.20-linux.tar.gz -O /tmp/android-studio.tar.gz && \
    mkdir -p /opt/android-studio && \
    tar -xzf /tmp/android-studio.tar.gz -C /opt/android-studio && \
    rm /tmp/android-studio.tar.gz

# Add Android Studio to PATH
ENV PATH="/opt/android-studio/bin:${PATH}"

# Expose Android Studio
CMD ["studio.sh"]
