FROM python:3.11

COPY requirements.txt /opt
COPY test.py /opt
RUN pip install -r /opt/requirements.txt

WORKDIR /opt

CMD ["python", "/opt/test.py"]
# ENTRYPOINT [ "/opt/stomp.sh" ]