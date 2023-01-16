# DBT connect with PostgreSQL

## Pre requisites

- You must installed Docker 20 or later.
- You need to have installed Python 3.7 or later.

## Getting started
You need to create a database. Therefore, we'll docker for create a container that has a Postgres database. It's therefore you must run te following command [database/run.sh](https://github.com/lbarreraabarca/neuralworks-challenge/blob/main/database/run.sh):

```bash
bash database/run.sh
```

You can validate that database is working:
```bash
docker ps -a
```

## DBT Environment
You need to create a virtual environment.
```bash
python -m venv dbt-venv
source dbt-venv/bin/activate
pip install -r requirements.txt
```

If you need your pipelines. Run the following steps:
```bash
cd jaffle_shop
dbt debug
dbt test
dbt run
```


