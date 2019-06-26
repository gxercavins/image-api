FROM debian:wheezy

#TODO: Use alpine (some issues with dependencies tho)
FROM python:3.6

# Copy the respective files into their directories
WORKDIR /app
COPY . /app

# Install system dependencies
#
#	Python dependencies
#		python-dev python-pip python-setuptools
#
#	Scrapy dependencies
#		libffi-dev libxml2-dev libxslt1-dev
#
#	Pillow (Python Imaging Library) dependencies
#		libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev
# 		liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
#

RUN apt-get update && apt-get install -y \
			python-dev python-pip python-setuptools \
			libffi-dev libxml2-dev libxslt1-dev \
			libtiff5-dev libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev \
			liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk

# Add the dependencies to the container and install the python dependencies
ADD requirements /tmp/requirements.txt
RUN pip install numpy
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
RUN pip install Pillow

# Expose web GUI
EXPOSE 5000

CMD [ "python", "app.py" ]
