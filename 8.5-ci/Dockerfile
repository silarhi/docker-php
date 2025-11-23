FROM php:8.5-alpine

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
RUN install-php-extensions intl opcache zip
