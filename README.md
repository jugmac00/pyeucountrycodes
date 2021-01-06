[![CI via GitHub Actions](https://github.com/jugmac00/pyeucountrycodes/workflows/CI/badge.svg)](https://github.com/jugmac00/pyeucountrycodes/actions?query=workflow%3ACI)
[![Current version on PyPI](https://img.shields.io/pypi/v/pyeucountrycodes.svg)](https://pypi.org/project/pyeucountrycodes/)
[![Requirements Status](https://requires.io/github/jugmac00/pyeucountrycodes/requirements.svg?branch=master)](https://requires.io/github/jugmac00/pyeucountrycodes/requirements/?branch=master)
![](https://img.shields.io/pypi/l/pyeucountrycodes.svg)

# pyeucountrycodes

A list of EU country codes following the ISO 3166-1 / Alpha-2 code.

## usage

```bash
pip install pyeucountrycodes

>>> from eu_country_codes import COUNTRY_CODES
>>> "FR" in COUNTRY_CODES
True
```


## scope

It is intended to keep this package very simple.

If you need to access the names of the countries, maybe even in different languages, please refer to the excellent **pycountry**:

https://pypi.org/project/pycountry/

## word of caution

Please note, that although Great Britain left the EU,
e.g. Northern Ireland is still treated - partly - as if it would still belong to the EU.


## contribution, feature requests and bug reports

Please use https://github.com/jugmac00/pyeucountrycodes


## development and run tests

```
$ python3 -m venv .venv
$ . .venv/bin/activate

$ pip install -U pip
$ pip install flit pytest

$ git clone git@github.com:jugmac00/pyeucountrycodes.git
$ cd pyeucountrycodes/
$ flit install

$ pytest .
```

## release history

### unreleased

Update development documentation.

Do not use Travis CI any more.

### 1.0.1 (04.01.2020)

Update readme for release.
### 1.0.0 (04.01.2020)

Test with GitHub actions.

Add support for Python 3.7, 3.8 and 3.9.

Drop support for Python 2.

Update usage example.

Remove GB from the list of EU countries.

### 0.7.0 (15.01.2019)

Initial release.

## sources

List of countries:

https://en.wikipedia.org/wiki/Member_state_of_the_European_Union (visited on 04.01.2021)

Iso codes:

https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes (visited on 15.01.2019)
