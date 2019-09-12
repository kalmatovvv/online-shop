#!/bin/bash

sudo mysql -uroot <<MYSQL_SCRIPT
CREATE DATABASE IF NOT EXISTS shop \
        DEFAULT CHARACTER SET utf8 \
        DEFAULT COLLATE utf8_general_ci;
CREATE USER IF NOT EXISTS 'shop_admin'@'localhost' IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON shop.* TO 'shop_admin'@'localhost';
FLUSH PRIVILEGES;
MYSQL_SCRIPT