
FROM python:3.12-slim

COPY  . /BE
RUN pip install fastapi pydantic uvicorn numpy argparse opencensus-ext-azure loguru
ENTRYPOINT ["python","/BE/calculator.py"]
