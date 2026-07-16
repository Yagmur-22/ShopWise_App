# ShopWise — сравнение цен (RU / EN)

## Описание (Russian)

ShopWise — простое настольное приложение на Python с графическим интерфейсом (Tkinter) для сравнения товаров (в проекте — ноутбуки и принтеры). Приложение загружает данные из парсеров и отображает их в таблице с возможностью сортировки, поиска и обновления базы.

Ключевая логика:
- `main.py` — GUI-приложение (Tkinter). Интерфейс: главная страница, экран ноутбуков, экран принтеров, сортировка, поиск, кнопки "ОБНОВИТЬ БАЗУ".
- `site_parsing.py` — парсинг/обновление данных (вызывается из `main.py`).
- Доп. файлы: `notebookmerkezi.py`, `nts_computer.py` и CSV-файлы (`comparison_result.csv`, `nts_computers.csv`, и т. п.) используются как источники/результаты данных.

Функции:
- Обновление базы товаров (через кнопку или вызов функции парсинга).
- Отображение таблицы сравнения из `comparison_result.csv`.
- Сортировка по ценам, алфавиту, наличию.
- Поиск по названию товара.

## Как запустить (Russian)

Требования:
- Python 3.8+ (рекомендуется 3.10+)
- Пакеты: `pandas`, `Pillow` (Tkinter обычно входит в стандартную поставку Python на Windows).

Установка зависимостей (рекомендуется в виртуальном окружении):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas pillow
```

Запуск приложения:

```bash
python main.py
```

Примечания:
- Для обновления данных нажмите кнопку "ОБНОВИТЬ БАЗУ" в интерфейсе или запустите соответствующие функции в `site_parsing.py` вручную.
- Если отображение кнопок использует иконки, убедитесь, что файлы изображений (например, `ОБНОВИТЬ БАЗУ (значок).png`, `ПОИСК (значок).png`) находятся рядом с `main.py`.

## Project structure (Russian)

- `main.py` — GUI
- `site_parsing.py` — парсеры/обновление
- `notebookmerkezi.py`, `nts_computer.py` — вспомогательные парсеры
- `comparison_result.csv` — результат сравнения/таблица
- другие утилиты/скрипты — вспомогательные

---

## Description (English)

ShopWise is a small Python desktop application (Tkinter) for comparing products (current focus: notebooks and printers). The app collects data via scrapers/parsers and displays a comparison table with sorting, searching, and update capabilities.

Main components:
- `main.py` — GUI (Tkinter). Provides home screen, notebooks and printers screens, sorting, search, and "UPDATE DATABASE" buttons.
- `site_parsing.py` — data parsing/updating logic (invoked from `main.py`).
- Additional scripts: `notebookmerkezi.py`, `nts_computer.py` and CSV files (`comparison_result.csv`, `nts_computers.csv`, etc.) used as data sources/results.

Features:
- Update product database via UI or parser functions.
- Display comparison table from `comparison_result.csv`.
- Sorting by price, name, availability.
- Search by product name.

## How to run (English)

Requirements:
- Python 3.8+ (3.10+ recommended)
- Packages: `pandas`, `Pillow` (Tkinter is usually included with Python on Windows).

Install dependencies (use virtual environment):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas pillow
```

Run the app:

```bash
python main.py
```

Notes:
- To refresh data click "ОБНОВИТЬ БАЗУ" in the UI or run parser functions in `site_parsing.py` directly.
- If the UI uses icon images, ensure image files (e.g. `ОБНОВИТЬ БАЗУ (значок).png`, `ПОИСК (значок).png`) are present next to `main.py`.

## Tech stack

- Python
- Tkinter (GUI)
- pandas (data handling)
- Pillow (image handling in GUI)

---

If you want, I can:
- добавить `requirements.txt` и пример виртуального окружения,
- оформить более подробную документацию по парсерам и CSV-форматам,
- подготовить инструкции по тестированию и CI.

Автор: локальный проект
