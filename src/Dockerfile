FROM python:3.12-slim

WORKDIR /app

# Copia arquivos de dependências
COPY app/api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia toda a aplicação
COPY app/ .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]