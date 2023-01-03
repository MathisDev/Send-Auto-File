FROM python:3.10
WORKDIR /app
COPY . /app
EXPOSE 80
CMD ["cd","/app","&&","bash","bash.sh","&&","python3","py.py"]
