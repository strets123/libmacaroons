FROM python:3.5
RUN apt-get update 
RUN apt-get install -y software-properties-common
RUN pip install Cython
COPY . /macaroons
#COPY bindings/python/libmacaroons.pyx /macaroons/

WORKDIR /macaroons


RUN  python setup.py install

RUN python -c "from macaroons import Verifier;from macaroons import create"

