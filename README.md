# E-commerce Backend

This is a Django-based e-commerce backend application built with Django REST Framework (DRF) and OAuth2 for authentication. It includes modules for product management, orders (sales and purchases), notifications for low-stock products, and background tasks using Celery. The app is designed to be secure, modular, and scalable, with additional features such as unit testing, caching, and performance optimizations.

## Features

- **Product Management**: CRUD operations for products (name, description, price, stock, SKU).
- **Sales Orders**: Create sales orders and reduce product stock.
- **Purchase Orders**: Create purchase orders to restock inventory.
- **Inventory Management**: Automatically update stock after sales and purchases.
- **Low-Stock Notifications**: Notify admin when product stock falls below a threshold.
- **OAuth2 Authentication**: Secure API with OAuth2 using Django OAuth Toolkit.
- **API Documentation**: Swagger and Redoc for API documentation.
- **Background Tasks**: Scheduled tasks using Celery for low-stock notifications.
- **Unit Testing**: Comprehensive unit tests for API endpoints and authentication.
- **Caching**: Basic caching mechanism for frequently accessed endpoints.
- **Docker**: Dockerized for easy deployment in different environments (development/production).

## Table of Contents

1. [Installation](#installation)
2. [Running the Application](#running-the-application)
3. [API Endpoints](#api-endpoints)
4. [Authentication](#authentication)
5. [Scheduled Tasks](#scheduled-tasks)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Contributing](#contributing)

## Installation

### Prerequisites

- **Python 3.8+**
- **Docker** and **Docker Compose**
- **PostgreSQL**
- **Redis** (for Celery and task queues)

### Clone the Repository

```bash
git clone https://github.com/essam5/ecommerce-backend.git
cd ecommerce-backend
```

## Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Set Up the Database

```bash
python manage.py migrate
```

## Create a Superuser

```bash
python manage.py createsuperuser
```

## Start the Django Development Server

```bash
python manage.py runserver
```

## Using Docker

1. **Build the Docker Image**

```bash
docker build -t ecommerce-backend .
```

2. **Run the Docker Container**

```bash
docker-compose up -d
```

3. **Access the Application**
   - The application will be accessible at http://localhost:8000.

### API Documentation

## Swagger and Redoc are set up for API documentation.

- **Swagger UI**: Accessible at http://localhost:8000/swagger/
- **Redoc**: Accessible at http://localhost:8000/redoc/

## Scheduled Tasks

- Low-stock notifications are handled by Celery. You can run the Celery worker and beat scheduler with:

```bash
celery -A ecommerce_backend worker --loglevel=info
celery -A ecommerce_backend beat --loglevel=info

```

## Testing

1. **Run unit tests**

```bash
python manage.py test
```

2. **OR Run Tests with Docker**

```bash
docker-compose run web python manage.py test
```
