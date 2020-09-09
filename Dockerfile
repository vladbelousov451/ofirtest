FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r ./requirement.txt
EXPOSE 80 
ENTRYPOINT [ "python" ] 
CMD [ "test.py" ]