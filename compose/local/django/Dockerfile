FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Git dependency for some requirements
  && apt-get install -y git \
  # Translations dependencies
  && apt-get install -y gettext \
  # Install ffmpeg
  && apt-get install -y ffmpeg \
  # install ssh - only do it if necessary
  && apt-get install -y git curl openssh-client \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# use this command only to test installing packages in private repo
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts

# Requirements are installed here to ensure they will be cached.
RUN pip install poetry
COPY poetry.lock pyproject.toml /requirements/
WORKDIR /requirements
RUN poetry config virtualenvs.create false 
RUN --mount=type=ssh poetry install --no-interaction --no-ansi

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY config /app
COPY soundscribe_webui /app

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
