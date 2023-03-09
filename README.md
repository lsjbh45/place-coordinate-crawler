# Place Coordinate Crawler

Developed for automatic coordinate info collecting process of ["한그릇" application](https://apps.apple.com/kr/app/%ED%95%9C%EA%B7%B8%EB%A6%87/id6443803936)

## Description

This program automatically:

- Save the coordinate info (latitude and longitude) into the database
  - Based on the address of the place
  - Using Kakao Local Rest API ([API Docs](https://developers.kakao.com/docs/latest/ko/local/dev-guide#address-coord))
  - If the coordinate of the place is not already staged in the database

## Prerequisites

- `pip` should be installed

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Configuration with `.env` file should be done before running the app.

### How to configure

Construct `key = value` style configuration

- At: `.env` file
- About:
  - `HOST`, `PORT`, `USER`, `PASSWORD`, `DATABASE`: Database configurations
  - `TOKEN`: Kakao REST API Authorization key ([Issuance](https://developers.kakao.com/))
  - `TABLE`, `pk_col`, `ADDRESS_COL`, `LATITUDE_COL`, `LONGITUDE_COL`: Target table / column names of database

### Example configuration

```
HOST="localhost"
PORT=5432
USER="postgres"
PASSWORD="postgres"
DATABASE="postgres"
TOKEN="8m1ywk23uphvli9pvlin15006r1s0mfp"
TABLE="place"
PK_COL="id"
ADDRESS_COL="address"
LATITUDE_COL="latitude"
LONGITUDE_COL="longitude"
```

## Running the app

```bash
py main.py
```

## Checking the execution logs

```bash
less log.txt
```
