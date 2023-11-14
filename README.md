## Init Project

* create virtual environment
```bash
python -m venv favenv
```
* activate virtual environment
```bash
source favenv/bin/activate
```
* install requirements
```bash
pip install fastapi
```

* build fastapi image
```bash
docker build -t fastapi -f fastapi.Dockerfile .
```

* run fastapi container
```bash
docker run -d -p 8000:8000 fastapi
```