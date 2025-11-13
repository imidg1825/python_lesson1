# Lesson 1 — Домашнее задание

Папка содержит решения заданий 1–5 и базовую конфигурацию **flake8**.

## Состав
- `lesson_1_task_1.py` — переменная `my_name = "Иван Мазницын"` и её вывод.
- `lesson_1_task_2.py` — переменная `my_age = 42`, затем возраст через 3 года, вывод.
- `lesson_1_task_3.py` — ввод `first_name` и `last_name` через `input()`, вывод в формате «Вас зовут: Фамилия Имя».
- `lesson_1_task_4.py` — функция `print_greeting()` печатает «Привет, мир!», вызов из `__main__`.
- `lesson_1_task_5.py` — параметризованная функция; 11 вызовов печатают `88005553535`.
- `.flake8` — настройки линтера (**PEP 8**).

## Как запускать в VS Code
1. Включите автосохранение: **Файл → Автосохранение**.
2. Откройте нужный файл и нажмите ▶️ (или **Terminal → Run Python File**).
3. В задании 3 консоль запросит имя и фамилию.

## Проверка стилем (flake8)
Из корня проекта выполните:
```bash
flake8 01_lesson
```

## Git и Pull Request
```bash
git checkout -b lesson1
git add 01_lesson
git commit -m "Lesson 1: tasks 1–5 + flake8 + README"
git push -u origin lesson1
```
Затем на GitHub создайте **Pull Request** из `lesson1` в `master`/`main` и сдайте ссылку вида `https://github.com/.../.../pull/N`.
