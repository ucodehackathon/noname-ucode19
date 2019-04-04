#!/bin/bash

composer update
composer install
cp .env.example .env
touch database/database.sqlite
php artisan migrate:refresh --seed
php artisan key:generate