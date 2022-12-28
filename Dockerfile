# syntax=docker/dockerfile:1

FROM python:3

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the Application
COPY src/test.py .
CMD [ "python", "test.py" ]