FROM ubuntu:20.04 as system

LABEL maintainer="daniel0392@gmail.com"
LABEL version="0.1"
LABEL description="Custom Docker image for \
the ROS training at IWT Bodensee."

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV ROS_DISTRO noetic

RUN apt update

RUN apt-get update

RUN apt update && \ 
	apt install -y software-properties-common
RUN add-apt-repository universe

RUN apt-get update && apt-get install -y curl gnupg lsb-release cmake git vim python3-pip python3-setuptools wget 

RUN DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration && \
	echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list && \
	apt-get install -y curl && \
	#curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
	wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc && \
	apt-key add ros.asc && \
	apt-get update && \
	apt-get install -y ros-noetic-desktop-full

RUN echo . "/opt/ros/$ROS_DISTRO/setup.sh" >> ~/.bashrc
