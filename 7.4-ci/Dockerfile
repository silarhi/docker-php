FROM mlocati/php-extension-installer:latest AS php-extension-installer
FROM php:8.3-alpine

ENV COMPOSER_ALLOW_SUPERUSER=1

WORKDIR /app

HEALTHCHECK --interval=1m --timeout=3s --start-period=5s --start-interval=1s --retries=3 \
    CMD curl -f http://localhost/_health || exit 1

SHELL ["/bin/ash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apk add --no-cache \
    bash \
    git \
    icu

# PHP Extensions
COPY --from=php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/
RUN install-php-extensions @composer intl opcache zip
