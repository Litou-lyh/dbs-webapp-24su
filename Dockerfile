##################################################
# Create production image
##################################################
FROM python:3.11-slim

# Establish a working folder
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Initialize the database and start PostgreSQL
RUN service postgresql start && \
    service postgresql start && \
    su postgres -c "psql -c \"ALTER USER postgres WITH PASSWORD 'pgs3cr3t';\"" && \
    su postgres -c "createdb petstore"

# Install Python dependencies
COPY pyproject.toml poetry.lock ./
RUN python -m pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --without dev

# Copy source files
COPY wsgi.py .
COPY service ./service
COPY checkpoints ./checkpoints

# Expose any ports the app is expecting in the environment
ENV FLASK_APP=wsgi:app
ENV PORT 8080
EXPOSE $PORT

# Set environment variable for PostgreSQL
ENV PGHOST=127.0.0.1
ENV PGUSER=postgres
ENV PGDATABASE=petstore
ENV PGPASSWORD=pgs3cr3t
ENV PGPORT=5432

# Run both PostgreSQL and the Python application
CMD service postgresql start && gunicorn --log-level=info wsgi:app

