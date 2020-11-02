FROM ubuntu

WORKDIR /usr/src/app
COPY . .
RUN apt-get -y update

RUN apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& apt-get install -y git \
&& apt-get install -y vim \
&& pip3 install -r requirements.txt \
&& git config --global user.name victor_ml \
&& git config --global user.email victor@test.fr \
&& git clone https://github.com/vuitor/python_m2.git

EXPOSE 8000
CMD ["jupyter", "notebook", "--port=8000", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
