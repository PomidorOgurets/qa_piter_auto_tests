<h1 >Проект автоматизации тестирования сайта <a href="https://piter-online.net/leningradskaya-oblast">piter-online.net</a></h1>

## Содержание

* <a href="#annotation">Описание</a>
* <a href="#tools">Технологии и инструменты</a>
* <a href="#cases">Реализованные проверки</a>
* <a href="#requirements">Установка зависимостей</a>
* <a href="#console">Запуск тестов из терминала</a>

<a id="annotation"></a>
## Описание
Тестовый проект состоит из веб-тестов (UI)
Краткий список интересных фактов о проекте:
- [x] Проект написан на Playwright - фреймворке для тестирования современных веб‑приложений.
- [x] Возможность запуска как всех тестов сразу, так и отдельных
- [x] `Page Object` проектирование

<a id="tools"></a>
## Технологии и инструменты

<div align="center">
<a href="https://github.com/"><img alt="GitHub" height="50" src="logo_image/GitHub.png" width="50"/></a>  
<a href="https://www.python.org/"><img alt="Python" height="50" src="logo_image/python-original.png" width="50"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img alt="Pycharm" height="50" src="logo_image/pycharm-original.png" width="50"/></a>  
<a href="https://docs.pytest.org/en/stable/index.html#"><img alt="Pytest" height="50" src="logo_image/pytest-original.png" width="50"/></a>
<a href="https://playwright.dev/python/"><img alt="Playwright" height="50" src="logo_image/playwright.png" width="50"/></a>
</div>

Автотесты в этом проекте написаны на Python с использованием фреймворка [Playwright](https://playwright.dev/python/).\
<code>GitHub</code> — репозиторий для хранения кода и контроля версий.\
<code>Python</code> — основной язык программирования для автотестов.\
<code>PyCharm</code> — IDE для разработки и отладки тестов.\
<code>pytest</code> — фреймворк для запуска и организации тестов.\
<code>Playwright</code> — для кросс-браузерного тестирования веб-приложений.

<a id="cases"></a>
## Реализованные проверки

### Автоматизация подачи заявки
:heavy_check_mark: Ввод тестовых данных для создания заявки через форму на сайте

:heavy_check_mark: Подтверждение успешной отправки заявки (по появляющемуся заголовку с входными данными)

### Автоматизированная смена региона
:heavy_check_mark: Смена региона на сайте

:heavy_check_mark: Проверка, что регион сменился корректно

### Автоматизированная проверка HTTP-кода ответа страницы
:heavy_check_mark: Проверка, что главная страница сайта возвращает HTTP 200

### Стабильность выполнения
:heavy_check_mark: Автотесты выполняются 5 раз подряд и не падают

<a id="requirements"></a>
## Установка зависимостей
После клонирования репозитория необходимо:
* Находясь в нужной директории (qa_piter_auto_tests) запустить командую строку - cmd
* Установить playwright и pytest через cmd - <code>pip install pytest-playwright</code>

<a id="console"></a>
## Запуск тестов из терминала
* Запустить все тесты через cmd - <code>pytest .\test_piter.py</code>
* Запуск теста подачи заявки 5 раз - <code>pytest test_piter.py::test_fill_page -v</code>
* Запуск теста смены региона 5 раз - <code>pytest test_piter.py::test_change_region -v</code>
* Запуск теста проверки HTTP-кода ответа страницы 5 раз - <code>pytest test_piter.py::test_status -v</code>