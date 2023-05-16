# django-pos
Membuat POS sistem menggunakan Django v2.2


## 1. SETUP 


### 1.1 Membuat virtual environment dan menginstall django v2.2


## 2. MEMBUAT PROYEK DJANGO DAN APP


#### 2.1 Membuat proyek dengan nama config-pos

        modified:   README.md
        new file:   config_pos/__init__.py
        new file:   config_pos/asgi.py
        new file:   config_pos/settings.py
        new file:   config_pos/urls.py
        new file:   config_pos/wsgi.py
        new file:   manage.py


#### 2.2 Membuat (ulang) proyek dengan nama config-pos

        deleted:    config_pos/asgi.py
        modified:   config_pos/settings.py
        modified:   config_pos/urls.py
        modified:   config_pos/wsgi.py
        modified:   manage.py

        NOTE:

        Pada 2.1, saat membuat proyek, venv3932 tidak
        diaktifkan sehingga hasilnya tdk berfungsi.

        Oleh karena itu, pembuatan proyek diulang dengan
        prosedur yang bernar, yakni mengaktifkan terlebih
        dahulu venv3932.

        Testing: hasil bagus :)


#### 2.3 Create, Connect db and settings

        modified:   .gitignore
        modified:   README.md
        modified:   config_pos/settings.py

