FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN python -m venv venv && /bin/bash -c "source venv/bin/activate" && pip install --no-cache-dir -r venv_requirements

CMD [ "gunicorn", "app:app", "-c", "./config/gunicorn_conf.py" ]