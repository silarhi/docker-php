FROM php:8.2-alpine

ENV COMPOSER_ALLOW_SUPERUSER=1

WORKDIR /app

HEALTHCHECK --interval=1m --timeout=3s --start-period=5s --start-interval=1s --retries=3 \
    CMD curl -f http://localhost/_health || exit 1

# Install dependencies
RUN apk add --no-cache \
    bash \
    icu \
    libxml2 \
    libzip \
    git \
    zlib && \
    #Composer
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# PHP Extensions
ENV PHPIZE_DEPS="\
    autoconf \
    cmake \
    file \
    freetype-dev \
    g++ \
    gcc \
    icu-dev \
    libc-dev \
    libzip-dev \
    make \
    pcre-dev \
    pkgconf \
    re2c \
    zlib-dev"

RUN apk add --no-cache --virtual .build-deps \
    $PHPIZE_DEPS && \
    docker-php-ext-install -j$(nproc) intl opcache zip && \
    apk del .build-deps && \
    rm -rf /var/cache/apk/* /tmp/*
