FROM python:3.10-bookworm
RUN mkdir -p /home/app
WORKDIR /home/app
COPY . /home/app
RUN  pip install --upgrade pip
RUN pip install -r /home/app/requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501"]