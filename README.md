# Automation Testing (Python)
---

E2E testing project with Python and Selenium


### Getting Started

- Install **Python 3** - Download **Python 3** [Click here](https://www.python.org/downloads/)


- In order to verify the successful installation of **python 3**, run in terminal below commands:

```console
python3 --version
```

```console
pip3 --version
```


- Install all dependences in _(requirements.txt)_

```console
pip3 install -r requirements.txt
```


### Supported Browsers

- CHROME
- FIREFOX


### Arguments

- Choose environment such as __qa__, __stage__
```
python3 runner.py qa
python3 runner.py stage
```


### Running the Tests

- Run all tests passing __qa__ environment _(Test Suite)_

```console
python3 runner.py qa
```

- Run single tests

```console
python3 -m unittest tests/test_login.py
python3 -m unittest tests/test_registration.py
```
