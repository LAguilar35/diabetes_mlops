FROM python:3.9-slim

WORKDIR /app

COPY trained_model.pkl /app/
COPY main.py /app/

RUN pip install fastapi uvicorn scikit-learn pydantic category_encoders joblib pandas

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]