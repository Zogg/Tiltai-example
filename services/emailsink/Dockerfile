FROM zogg/nanomsg

WORKDIR /myproject

COPY requirements.txt /myproject/requirements.txt
RUN pip install -r requirements.txt

COPY ./src /myproject

ENTRYPOINT ["python", "-u", "run.py"]
