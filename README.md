# datanorge
Repo for publisering og høsting til datanorg


## Sette opp pythonmiljø
Sett opp virituelt miljø

```sh
brew update && brew install pyenv
pyenv install 3.10
```

```sh
pyenv local 3.10
```

```sh
pyenv exec python3 -m venv .venv
source .venv/bin/activate
```

Installer avhengigheter
```sh
pip3 install -r requirements.txt
```

Kjør main
```sh
python3 -m src.main
```

