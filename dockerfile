FROM python:3.11

WORKDIR /app

# 依存関係のコピーとインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . /app/

# 開発用サーバーの起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]