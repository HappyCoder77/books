FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd -g 1000 djangouser && \
    useradd -m -u 1000 -g djangouser djangouser

COPY Pipfile Pipfile.lock /app/

RUN pip install --no-cache-dir pipenv &&\
    pipenv install --system --deploy

COPY --chown=djangouser:djangouser . /app/

USER djangouser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
