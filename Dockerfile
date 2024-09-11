FROM python:3.12
RUN pip install poetry
COPY . /project
WORKDIR /project
RUN poetry install
EXPOSE 8501
ENTRYPOINT [ "poetry", "run", "uvicorn", "src.controller:app", "--host", "0.0.0.0", "--port", "8501" ]
