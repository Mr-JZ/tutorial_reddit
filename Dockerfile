FROM python:3.10

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /src

COPY ./setup.py .
COPY ./setup.cfg .

RUN pip3 install -e .

CMD ["uvicorn", "src.api.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "7000"]