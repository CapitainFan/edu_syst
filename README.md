# Edu_syst API

Этот проект представляет собой API для управления школой, включая информацию о школах, классах, учителях и учениках. API построен на Django Rest Framework (DRF) и предоставляет эндпоинты для регистрации пользователей, аутентификации, а также для управления данными о школах, классах, учителях и учениках.

---

## Описание проекта

Проект позволяет:
- Регистрировать пользователей (учеников и учителей).
- Аутентифицировать пользователей с помощью JWT-токенов.
- Управлять данными о школах, включая список классов, учителей и учеников.
- Получать информацию о классах и их учениках.
- Управлять данными о учителях и учениках.

---

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:CapitainFan/edu_syst.git
   cd edu_syst
2. Установите виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate```
-
    если Windows
   ```bash
   python -m venv venv
   venv\Scripts\activate.bat```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
4. Перейдите в папку с кодом и сделайте миграции:
   ```bash
   cd edu_syst
   python manage.py migrate
5. Сайт готов к запуску:
   ```bash
    python manage.py runserver
## Эндпоинты API

### Аутентификация и регистрация

- **Регистрация нового пользователя**  
  ```bash
  POST http://127.0.0.1:8000/api/register/
-  
  **Параметры:**  
  - ```username```  
  - ```email```  
  - ```password```  
  - ```user_type``` (```student```, ```teacher```, ```user```)  
  - ```school_id``` (опционально)  
  - ```form_id``` (опционально)

- **Получение JWT-токена**  
  ```bash
  POST http://127.0.0.1:8000/api/token/
-
  **Параметры:**  
  - ```username```  
  - ```password```

- **Обновление JWT-токена**  
  ```bash
  POST http://127.0.0.1:8000/api/token/refresh/
-
  **Параметры:**  
  - ```refresh``` (refresh token)

---

### Школы

- **Получить список всех школ**  
  ```bash
  GET http://127.0.0.1:8000/api/schools/

- **Получить информацию о конкретной школе**
  ```bash
  GET http://127.0.0.1:8000/api/schools/{pk}/

- **Получить список классов в школе**
  ```bash
  GET http://127.0.0.1:8000/api/schools/{pk}/get_list_of_forms/

- **Получить список учителей в школе**  
  ```bash
  GET http://127.0.0.1:8000/api/schools/{pk}/get_list_of_teachers/

- **Получить список учеников в школе**  
  ```bash
  GET http://127.0.0.1:8000/api/schools/{pk}/get_list_of_students/

---

### Классы (Forms)

- **Получить список всех классов**  
  ```bash
  GET http://127.0.0.1:8000/api/forms/

- **Получить информацию о конкретном классе**  
  ```bash
  GET http://127.0.0.1:8000/api/forms/{pk}/

- **Получить список учеников в классе**  
  ```bash
  GET http://127.0.0.1:8000/api/forms/{pk}/get_list_of_students/

---

### Учителя

- **Получить список всех учителей**  
  ```bash
  GET http://127.0.0.1:8000/api/teachers/

- **Получить информацию о конкретном учителе**  
  ```bash
  GET http://127.0.0.1:8000/api/teachers/{pk}/

---

### Ученики

- **Получить список всех учеников**  
  ```bash
  GET http://127.0.0.1:8000/api/students/

- **Получить информацию о конкретном ученике**  
  ```bash
  GET http://127.0.0.1:8000/api/students/{pk}/
---

## Примеры запросов

### Регистрация нового пользователя (учителя)
    POST /api/register/
    {
        "username": "teacher1",
        "email": "teacher1@example.com",
        "password": "password123",
        "user_type": "teacher",
        "school_id": 1
    }

### Получение JWT-токена
    POST /api/token/
    {
        "username": "teacher1",
        "password": "password123"
    }

### Получение списка школ
    GET /api/schools/


### Получение списка учеников в классе
    GET /api/forms/1/get_list_of_students/

# Авторы
Богдан Сокольников.