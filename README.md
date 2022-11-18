
# Xerpa Test

Proyecto prueba 2 Xerpa


## Authors

- [@jorgegpsm](https://www.github.com/jorgegpsm)

## API Reference

Se adjunta el archivo Postman con el REST Xerpa.postman_collection.json

**==================Players*====================*
#### Get Players
```http
  GET /players
```

#### Get Player

```http
  GET /players?player=1
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `teams`      | `string` | **Required**. Id of item to fetch |


#### POST Player

```http
  POST /players
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name Player|
| `goals`      | `number` | **Required**. Goals Player |
| `team_id`      | `number` | **Required**. TeamID Team |


#### Update Player

```http
  UPDATE /players
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `number` | **Required**. ID Player |
| `name`      | `string` | **Required**. Name Player|
| `goals`      | `number` | **Required**. Goals Player |
| `team_id`      | `number` | **Required**. TeamID Team |

#### Delete Player

```http
  DELETE /players
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

*================== Teams ====================*
#### Get Players
```http
  GET /teams
```

#### Get Player

```http
  GET /teams?teams=1
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `teams`      | `string` | **Required**. Id of item to fetch |


#### POST Player

```http
  POST /teams
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `number` | **Required**. ID Team |
| `name`      | `string` | **Required**. Name Team|
| `city`      | `number` | **Required**. City Team |


#### Update Team

```http
  UPDATE /teams
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `number` | **Required**. ID Team |
| `name`      | `string` | **Required**. Name Team|
| `city`      | `number` | **Required**. City Team |

#### Delete Team

```http
  DELETE /teams
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


## Tech Stack

**SQL:** Postgresql

**Server:** Python, Django

**Infra:** Docker

## Installation

Required postgresql running in docker or localhost

Database
```POSTGRESQL
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'cr255root',
    'HOST': '127.0.0.1',
    'PORT': '5432',
```

Django docker
```DJANGO
    python manage.py makemigrations Players
    python manage.py makemigrations Teams
    python manage.py migrate
    docker run -d -p 80:80 --name proyect-xerpa --restart always proyect-xerpa
```