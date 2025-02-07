FROM python:3.9

WORKDIR /app
COPY . /app

RUN curl -LO https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.macos-cocoa.pkg
RUN sudo installer -pkg wkhtmltox-0.12.6-1.macos-cocoa.pkg -target /

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "3000"]
