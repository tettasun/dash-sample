# The Dockerfile defines the image's environment
# Import Python runtime and set up working directory
FROM python:3.6-alpine
WORKDIR /work
ADD . /work

# Install any necessary dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Open port 8050 for serving the webpage
EXPOSE 8050

# Run app.py when the container launches
CMD ["python", "server/src/app.py"]
