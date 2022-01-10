FROM python:3.10.1
WORKDIR /app
COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . .
CMD streamlit run App.py

