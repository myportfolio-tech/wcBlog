# Base UBuntu Image
FROM ubuntu

# PYthon Installation
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

# Copy Source Code
WORKDIR /web
COPY . /web
RUN file="$(ls -al)" && echo $file
# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN python3 setup.py
# Expose Ports
# EXPOSE 8000

# Launch App with gUnicorn
# ENTRYPOINT ["python3"]
