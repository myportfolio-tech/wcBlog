# Base UBuntu Image
FROM ubuntu

# PYthon Installation
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

# Copy Source Code
WORKDIR /web
COPY . /web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=run.py

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 setup.py
# Expose Ports
EXPOSE 8000

# Launch App with gUnicorn or Run.py
# ENTRYPOINT ["python3", "run.py"]
#CMD ["flask", "run", "--host=0.0.0.0:8000"]
# CMD ["gunicorn" , "--reload", "--bind", "0.0.0.0:8000", "run:app"]