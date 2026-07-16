FROM python:3.11-slim

WORKDIR /app

# Ensure project root is on PYTHONPATH so `from src...` imports work
ENV PYTHONPATH=/app

# Copy project
COPY . /app

# Install runtime deps from requirements
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
