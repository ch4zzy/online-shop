# online-shop
Online shop realization.

## Features

### Product Catalog

Browse a wide selection of products with detailed information:

- **Product Details:** Each product includes images and comprehensive descriptions.
- **Clear Pricing:** Transparent pricing helps customers make informed choices.
- **Comments:** Type comment for any product.

### Shopping Cart

Easily manage selected items in your cart:

- **Add and Remove:** Effortlessly add or remove items from your cart.
- **Quantity Control:** Adjust quantities according to your preferences.
- **Total Cost:** View the total cost of selected items before checkout.

### Coupons

Each user can use coupons.
- **Manage coupons:** Create, update in admin panel.

### Checkout Process

Efficient and user-friendly checkout process:

- **Address Input:** Input your shipping address for accurate delivery.
- **Payment Options:** Choose from various payment methods.

### Admin Dashboard

Admin panel to manage products and orders:

- **Product Management:** Add, edit, and remove products.
- **Order Tracking:** Monitor and update order status.

### Order Confirmation Emails

Automatic order confirmation emails:

- **Instant Notifications:** Customers receive emails with order details after purchase.

## Setup

### Environment

All this environment need to be set up.

path: `config/.env`

```
# Django 

SECRET_KEY=
DEBUG=

# Database

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=

# Email

EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=
EMAIL_USE_TLS=

# OAuth

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=

# Braintree

BRAINTREE_MERCHANT_ID=
BRAINTREE_PUBLIC_KEY=
BRAINTREE_PRIVATE_KEY=
```

### Docker

clone repo: `git clone https://github.com/ch4zzy/online-shop.git`

build docker: `docker build .`

run docker: `docker-compose up -d`
