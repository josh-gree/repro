FROM prefecthq/prefect:2.10.12-python3.9

COPY . /opt/src

WORKDIR /opt/src
RUN pip install poetry && poetry build && pip install --verbose ./dist/*.whl