FROM python:3.9
WORKDIR /polarity_check_api
COPY . /polarity_check_api
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -c "import nltk; nltk.download('vader_lexicon')"
CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5050"]