#!/bin/bash

set -e

for version in *; do
	[ -d "$version" ] || continue
	[[ "$version" != "_shared" ]] || continue
	[[ "$version" != *"-ci" ]] || continue

	cp -R _shared/* "$version"

	if [[ "$version" == *"-symfony"* ]]; then
		mv "$version/conf/vhost-symfony.conf" "$version/conf/vhost.conf"
	else
		rm "$version/conf/vhost-symfony.conf"
	fi

	if [[ "$version" != *"-frankenphp"* ]]; then
    rm "$version/conf/Caddyfile" "$version/conf/symfony-worker.Caddyfile"
  else
    rm "$version/conf/apache.conf" "$version/conf/vhost.conf"
    rm -rf "$version/errors"
  fi
done
