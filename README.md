# Веб-приложение "Интернет-магазин электроники"

Задание - разработать проект «Интернет-магазин». Этот сервис позволяет автоматизировать процесс покупки товаров в магазине, минимизирует телефонные/почтовые контакты с покупателями за счет удобной подачи информации, дает возможность получения актуальных значений товарных остатков, повышает лояльность клиентов за счет высокого уровня обслуживания, а также обеспечивает администрации магазина централизованный доступ ко всей информации, связанной с покупкой товаров.

## Пользователь:
### Главная страница
<img src="/static/imagesREADME/main_page.png" width="870" height="415"/>

# 

### Страница регистрации
<img src="/static/imagesREADME/registration.png" width="873" height="370"/>

# 

### Страница авторизации пользователя
<img src="/static/imagesREADME/user_login.png" width="870" height="165"/>

# 

### Страница добавления товара в корзину
<img src="/static/imagesREADME/add_in_busket.png" width="870" height="380"/>

# 

###  Страница корзины
<img src="/static/imagesREADME/busket.png" width="870" height="330"/>


## Администратор:
### Страница авторизации администратора
<img src="/static/imagesREADME/admin_login.png" width="870" height="273"/>

# 

### Главная страница администратора
<img src="/static/imagesREADME/admin_main_page.png" width="870" height="208"/>

# 

### Страница товаров
<img src="/static/imagesREADME/admin_items.png" width="870" height="415"/>

# 

### Страница добавления товара 
<img src="/static/imagesREADME/admin_adding_item.png" width="870" height="415"/>

# 

### Страница заказов
<img src="/static/imagesREADME/admin_orders.png" width="870" height="251"/>

# 

### Страница добавления заказа 
<img src="/static/imagesREADME/admin_adding_order.png" width="870" height="415"/>

# Этапы разработки:
## 1. Объектная декомпозиция предметной области
### 1.1 Схема взаимодействия объектов пользователя
<img src="/static/imagesREADME/user_object_interaction.png" width="870" height="533"/>

# 

### 1.2 Схема взаимодействия объектов администратора
<img src="/static/imagesREADME/admin_object_interaction.png" width="870" height="700"/>


## 2. Проектирование структуры и компонентов программного продукта 
### 2.1 Диаграмма вариантов использования
<img src="/static/imagesREADME/use_case_diagram.png" width="870" height="504"/>

# 

### 2.2 Диаграмма классов концептуального уровня
<img src="/static/imagesREADME/conceptual_class_diagram.png" width="870" height="509"/>

# 

### 2.2 Диаграмма деятельности
<img src="/static/imagesREADME/diagram_of_activity.png" width="870" height="700"/>

# 

### 2.3 Диаграмма «сущность-связь» базы данных 
<img src="/static/imagesREADME/database_diagram.png" width="870" height="700"/>

# 


### 2.4 Диаграмма классов интерфейса пользователя
<img src="/static/imagesREADME/user_interface_class_diagram.png" width="870" height="492"/>

# 

### 2.5 Диаграмма классов интерфейса администратора
<img src="/static/imagesREADME/admin_interface_class_diagram.png" width="870" height="410"/>

# 


### 2.6 Граф состояний интерфейса пользователя
<img src="/static/imagesREADME/user_interface_graph.png" width="870" height="562"/>

# 

### 2.6 Граф состояний интерфейса администратора
<img src="/static/imagesREADME/admin_interface_graph.png" width="870" height="582"/>

# 

### 2.7 Диаграмма компоновки приложения
<img src="/static/imagesREADME/diagramm_of_application_layout.png" width="870" height="700"/>

# 

### 2.8 Диаграмма размещения приложения
<img src="/static/imagesREADME/diagramm_of_application_placement.png" width="870" height="319"/>


## How to deploy

MySQL:

```bash
$ sudo apt-get -y update
$ sudo apt-get install -y mysql-server && \
		mysql-client && \
		python3-dev && \
		libmysqlclient-dev && \
		build-essential

$ sudo mysql -u root -p

mysql> CREATE DATABASE IF NOT EXISTS shop \
		DEFAULT CHARACTER SET utf8 \
    		DEFAULT COLLATE utf8_general_ci;

mysql> CREATE USER IF NOT EXISTS 'shop_admin'@'localhost' IDENTIFIED BY '12345';
mysql> GRANT ALL PRIVILEGES ON shop.* TO 'shop_admin'@'localhost' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;
mysql> Ctrl+D
```

Django app:

```bash
$ cd ~
$ git clone https://github.com/chahkiev/online_shop.git
$ cd online_shop/
$ python3 -mvenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py makemigrations shop
$ python3 manage.py migrate
$ python3 manage.py runserver
```

#### OR:

```bash
$ cd ~
$ git clone https://github.com/chahkiev/online_shop.git
$ cd online_shop/deploy
$ bash ./createDB.sh
$ bash ./runApp.sh
```

#

### Стек технологий:
* Python3;
* Django - фреймворк на языке Python;
* MySQL - база данных;
* Github – репозиторий для кода.

# 

### СПИСОК ИСПОЛЬЗУЕМЫХ ИСТОЧНИКОВ
1. Э. Гамма, Р. Хелм, Р. Джонсон, Дж. Влиссидес. Приемы объектно-ориентированного проектирования. Паттерны проектирования. СПб: «Питер», 2007. С. 366. 
2.	С. Морето. Bootstrap By Example. «Издательские решения», 2016. 182 с.  ISBN: 9785447462314
3.	Э. Фримен, Э. Робсон, К. Сиерра. Head First Design Patterns: A Brain-Friendly Guide. Обновленное изд. СПб: «Питер», 2018. 656 с.  ISBN 978-5-496-03210-0
4.	Иванова Г.С. Технология программирования: учебник / Г.С. Иванова. 3-е изд., стер. М.: КНОРУС, 2016. 334 с. (Бакалавриат). ISBN 978-5-04734-7