FROM ubuntu:20.04


WORKDIR /home/root/gutendex

COPY requirements.txt requirements.txt

RUN apt-get update

RUN apt-get install curl -y

# Install pip
RUN apt-get install -y python3-pip

# Install dependencies
RUN pip install -r requirements.txt

# Export the environment variables
RUN export $(grep -v '^#' .env | xargs)


COPY . .

EXPOSE 5000


CMD ["bash","start.sh"]