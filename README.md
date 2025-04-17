# Mattermost API Test Suite

Данный проект включает автотесты для API Mattermost, которые покрывают:

 - аутентификацию,
 - управление каналами,
 - отправку и получение сообщений.

## Prerequisites

- Python 3.8 or higher
- Mattermost server running (local or remote)
- Access to Mattermost API

## Setup

1. Склонировать репозиторий
2. Создать виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Усиановить расширения:
   ```bash
   pip install -r requirements.txt
   ```
4. Создать `.env` файл в проект:
   ```
   MATTERMOST_URL=http://your-mattermost-server:8065
   TEST_USERNAME=your-test-username
   TEST_PASSWORD=your-test-password
   TEST_EMAIL=your-test-email@example.com
   ```

## Running Tests

Прогнать все тесты:
```bash
pytest
```

Запустить отдельно тесты каналов:
```bash
pytest tests/test_authentication.py
pytest tests/test_channels.py
```

Сгенерировать html шаблон:
```bash
pytest --html=report.html
```

## Test Coverage

### Аутентификация
 - Успешный вход с правильными учетными данными
 - Неудачная попытка входа с неверными учетными данными
 - Вход с пустыми учетными данными
 - Вход с отсутствующими учетными данными
 - Успешный выход из системы

### Channel Management
 - Создание нового канала
 - Создание дубликата канала
 - Отправка сообщений в канал
 - Получение сообщений из канала

## Test Structure

- `config.py`: файл конфигурации
- `tests/base.py`: Базовый класс
- `tests/test_authentication.py`: Аутентификации тест-кейсы
- `tests/test_channels.py`: Тест-кейсы каналов

## Troubleshooting

Если у вас возникнут какие-либо проблемы:
1. Убедитесь, что ваш самый важный сервер запущен и доступен
2. Проверьте конфигурацию `.env` файла конфигурации
3. Убедитесь что у вас есть правильные разрешения на самом сервере
4. Проверьте сообщения на наличие сообщений об ошибках