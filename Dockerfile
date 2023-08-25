FROM ubuntu
USER root
RUN ["/bin/bash", "-c", "apt-get update -y && apt-get install python3 -y && apt-get install python3-pip -y && pip3 install flask"]
ADD demo.py /home/
WORKDIR /home/
EXPOSE 5000
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["python3", "demo.py"]

