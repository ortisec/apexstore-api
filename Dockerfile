FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- System deps ----
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Install uv (global) ----
RUN curl -LsSf https://astral.sh/uv/install.sh | \
    UV_INSTALL_DIR=/usr/local/bin sh

# ---- Workdir ----
WORKDIR /app

# ---- Copy dependency files ----
COPY pyproject.toml uv.lock ./

# ---- Install dependencies (production only) ----
RUN uv sync --frozen

# ---- Copy application code ----
COPY app ./app

# ---- Expose port ----
EXPOSE 8000

# ---- Run app ----
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
