FROM python:3.9.18-alpine3.19

RUN apk update && apk upgrade
RUN apk add --no-cache gcc musl-dev libffi-dev curl

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV BOT_TOKEN=${BOT_TOKEN}
ENV ALLOWED_USERS=${ALLOWED_USERS}

COPY src/ ./src/

CMD ["python", "src/bot.py"]