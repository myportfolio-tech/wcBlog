# Base UBuntu Image
FROM ubuntu

# PYthon Installation
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

# Copy Source Code
WORKDIR /weblog
COPY . /weblog

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
# Expose Ports
EXPOSE 5000

# Launch App with gUnicorn
ENTRYPOINT ["python3"]
CMD ["run.py"]