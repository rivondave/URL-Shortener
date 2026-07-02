# URL Shortener API

A RESTful URL Shortener API built with FastAPI, PostgreSQL, SQLAlchemy, and Docker.

This project allows users to create shortened URLs, define custom aliases, set expiration dates, and track link analytics. It demonstrates backend engineering concepts such as database modeling, URL redirection, analytics tracking, validation, and containerized deployment.

## Live Demo

API Base URL:

https://url-shortener-a2fq.onrender.com

Swagger Documentation:

https://url-shortener-a2fq.onrender.com/docs

---

## Features

### URL Shortening

* Generate shortened URLs
* Support for custom aliases
* Unique short code generation
* URL validation

### URL Redirection

* Redirect users from short URLs to original URLs
* Fast and reliable redirect handling

### Analytics

* Track click counts
* View analytics for individual shortened URLs
* Monitor link usage

### Expiration Support

* Set expiration dates for shortened URLs
* Prevent access to expired links

### API Management

* Retrieve all shortened URLs
* Create new shortened URLs
* View analytics for specific links

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Render

---

## API Endpoints

### URL Management

| Method | Endpoint | Description      |
| ------ | -------- | ---------------- |
| GET    | /urls    | Get all URLs     |
| POST   | /urls    | Create short URL |

### Analytics

| Method | Endpoint                     | Description       |
| ------ | ---------------------------- | ----------------- |
| GET    | /urls/analytics/{short_code} | Get URL analytics |

### Redirection

| Method | Endpoint      | Description              |
| ------ | ------------- | ------------------------ |
| GET    | /{short_code} | Redirect to original URL |

### Root

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /        | API status  |

---

## Example Request

### Create Short URL

Request:

```json id="4dnw5w"
{
  "original_url": "https://example.com",
  "custom_alias": "example",
  "expires_at": "2026-12-31T23:59:59"
}
```

Response:

```json id="0r3dko"
{
  "short_code": "example",
  "short_url": "https://url-shortener-a2fq.onrender.com/example"
}
```

---

## Project Structure

```text id="7n40m3"
app/
├── api/
├── core/
├── models/
├── schemas/
├── main.py

Dockerfile
docker-compose.yml
requirements.txt
.env
```

---

## Environment Variables

Create a `.env` file:

```env id="m8z0lb"
DATABASE_URL=postgresql://postgres:password@localhost/url_shortener

SECRET_KEY=your_secret_key
```

---

## Local Installation

Clone the repository:

```bash id="qqr3sh"
git clone https://github.com/rivondave/URL-Shortener.git

cd URL-Shortener
```

Create a virtual environment:

```bash id="cmr6iz"
python -m venv venv
```

Activate the virtual environment:

```bash id="nwb4dy"
source venv/bin/activate
```

Install dependencies:

```bash id="yvxf9q"
pip install -r requirements.txt
```

Run the application:

```bash id="svu4ll"
uvicorn app.main:app --reload
```

Swagger Documentation:

```text id="d7yivx"
http://127.0.0.1:8000/docs
```

---

## Docker Setup

Build and run containers:

```bash id="2n7m7n"
docker compose up --build
```

Access API:

```text id="baf2zr"
http://localhost:8000
```

Swagger Documentation:

```text id="54j8xv"
http://localhost:8000/docs
```

---

## Example Workflow

1. Create a shortened URL.
2. Share the generated short link.
3. Users visit the short link.
4. The API redirects them to the original URL.
5. Analytics data is automatically updated.
6. View click statistics through the analytics endpoint.

---

## What I Learned

* REST API Design
* URL Redirection Logic
* Database Modeling with SQLAlchemy
* Input Validation
* Analytics Tracking
* PostgreSQL Integration
* Docker Containerization
* API Deployment with Render
* Backend Service Architecture

---

## Future Improvements

* User authentication and ownership of URLs
* QR code generation
* Rate limiting
* Redis caching
* Custom domains
* Advanced analytics dashboard
* Automated testing with Pytest

```
```

## Features

- Create shortened URLs with automatically generated short codes
- Support for custom URL aliases
- Redirect shortened URLs to their original destination
- Click tracking and analytics
- URL expiration support
- PostgreSQL database integration
- Dockerized for consistent deployment
- Redis caching for improved redirect performance
- Interactive API documentation with Swagger UI

### Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Redis
- Docker
- Render

## Redis Caching

The API uses Redis to cache URL lookups and improve redirect performance.

### How It Works

1. A user visits a shortened URL.
2. The application first checks Redis for the corresponding original URL.
3. If the URL is found in Redis (cache hit), the user is redirected immediately without querying PostgreSQL.
4. If the URL is not found (cache miss), the application retrieves it from PostgreSQL, stores it in Redis for future requests, and then redirects the user.

### Benefits

- Faster response times
- Reduced database load
- Improved scalability for frequently accessed URLs

### Cache Configuration

```python
redis_client.set(
    short_code,
    url.original_url,
    ex=3600
)
```

Cached URLs remain in Redis for 1 hour before expiring automatically.