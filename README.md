# nsq v1.3.0

## Provision local nsq cluster using Docker compose


```bash
docker compose up -d
```

create a 'test' topic

```bash
curl -d 'hello world 1' 'http://127.0.0.1:4151/pub?topic=test'
```

## Run a Python client as a 'test' topic listener

it will 'hang' in the Terminal until it receives message from 'test' topic

```bash
python3 -m venv env && source env/bin/activate

pip install -r requirements.py

python3 main.py
```

## post messages to 'test' topic

* in a new terminal

```bash
curl -d 'hello world 1' 'http://127.0.0.1:4151/pub?topic=test'

curl -d 'hello world 2' 'http://127.0.0.1:4151/pub?topic=test'
```

you'll see the messages get printed in the python script's shell

## admin panel

[http://localhost:417](http://localhost:4171)

## sources

[https://nsq.io/deployment/docker.html](https://nsq.io/deployment/docker.html)
