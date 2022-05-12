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
RUN python setup.py
# Expose Ports
EXPOSE 8000

# Launch App with gUnicorn
# ENTRYPOINT ["python3"]
CMD ["gunicorn" , "--reload", "--bind", "0.0.0.0:8000", "run:app"]