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


#### 2.7 Using Built-in class-based generic views

        modified:   README.md
        modified:   app/base/urls.py
        modified:   app/base/views.py


## 3. LOGIN / LOGOUT


### 3.1 Use LoginRequiredMixin to required login to view the home page

        class home_page(LoginRequiredMixin, TemplateView):
                template_name = 'base/index.html'
                login_url = '/admin'

        path('',views.home_page.as_view(),name="home_page")

        modified:   README.md
        modified:   app/base/views.py

        NOTE:

        1. If user not login, user will redirect to admin page to login
        2. Once user logged in successfully, user can view the home page 


### 3.2 Create users app and login/logout

        modified:   README.md
        modified:   app/base/urls.py
        modified:   app/base/views.py
        new file:   app/users/__init__.py
        new file:   app/users/admin.py
        new file:   app/users/apps.py
        new file:   app/users/migrations/__init__.py
        new file:   app/users/models.py
        new file:   app/users/tests.py
        new file:   app/users/urls.py
        new file:   app/users/views.py
        modified:   config_pos/settings.py
        modified:   config_pos/urls.py
        modified:   templates/partials/footer.html
        modified:   templates/partials/top_navbar.html
        new file:   templates/users/login.html
        new file:   templates/users/logout.html

        NOTE:

        1. Existing user can login via the login page
        2. After logging in, user redirect to home page
        3. Home page is now protected
        4. Logged in user can logout and after logged out,
           user redirect to login page

        ** To login via login page, user MUST NOT logged in via admin dashboard


### 3.3 Adding Alert message

        modified:   README.md
        modified:   templates/users/login.html

        <small class="text-danger">
            {% if form.errors %}
                {% for field in form %}
                    {% if field.errors %}
                        {% for error in field.errors %}
                            {{ error |escape }}
                        {% endfor %}
                    {% endif %}    
                {% endfor %}

                {% if form.non_field_errors %}
                    {% for error in form.non_field_errors %}
                        {{ error|escape }}
                    {% endfor %}
                {% endif %}

            {% endif %}
        </small>


## 4. KATALOG


#### 4.1 Membuat app dengan nama 'app\inventory'

        modified:   README.md
        new file:   app/inventory/__init__.py
        new file:   app/inventory/admin.py
        new file:   app/inventory/apps.py
        new file:   app/inventory/migrations/__init__.py
        new file:   app/inventory/models.py
        new file:   app/inventory/tests.py
        new file:   app/inventory/views.py


#### 4.2 Register inventory app

        modified:   README.md
        modified:   app/inventory/apps.py
        modified:   config_pos/settings.py


#### 4.3 Membuat AbstractModel

        modified:   README.md
        modified:   app/base/models.py


#### 4.4 Membuat Category model, menjalankan migrasi dan membuat CategoryView

        modified:   README.md
        modified:   app/inventory/admin.py
        new file:   app/inventory/migrations/0001_initial.py
        modified:   app/inventory/models.py
        modified:   app/inventory/views.py


#### 4.5 Membuat laman category_list urls, view, template

        new file:   app/inventory/urls.py
        modified:   config_pos/urls.py
        new file:   templates/inventory/category_list.html