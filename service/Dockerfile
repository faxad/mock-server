FROM python:3.9

WORKDIR /code

RUN <<EOF
pip install fastapi[standard]
pip install requests
EOF

COPY ./main.py /code/

CMD ["fastapi", "run", "main.py", "--port", "80"]