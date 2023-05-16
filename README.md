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


#### 2.4 Membuat app dengan nama 'app/base'

        modified:   README.md
        new file:   app/base/__init__.py
        new file:   app/base/admin.py
        new file:   app/base/apps.py
        new file:   app/base/migrations/__init__.py
        new file:   app/base/models.py
        new file:   app/base/tests.py
        new file:   app/base/views.py
        modified:   config_pos/settings.py


#### 2.5 Configuring static files

        modified:   .gitignore
        modified:   README.md
        new file:   app/base/urls.py
        modified:   app/base/views.py
        modified:   config_pos/settings.py
        modified:   config_pos/urls.py
        new file:   templates/base.html
        new file:   templates/base/index.html


#### 2.6 Template inheritance

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/base/index.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/head.html
        new file:   templates/partials/sidebar.html
        new file:   templates/partials/top_navbar.html