1. Создание SSH-ключа
SSH-ключ нужен для безопасного подключения к GitHub без ввода пароля.

Шаги:

Откройте терминал (Linux/macOS) или Git Bash (Windows).

Введите команду для генерации ключа:

ssh-keygen -t ed25519 -C "ваш_email@example.com"
Если система не поддерживает ed25519, используйте:

ssh-keygen -t rsa -b 4096 -C "ваш_email@example.com"
Нажмите Enter для сохранения ключа в стандартную папку (~/.ssh/).

При запросе введите пароль (опционально, но рекомендуется для безопасности).

Где ключи?

Публичный ключ: ~/.ssh/id_ed25519.pub (или id_rsa.pub)
Приватный ключ: ~/.ssh/id_ed25519 (или id_rsa)

2. Добавление SSH-ключа в аккаунт GitHub
Скопируйте публичный ключ в буфер обмена:

Linux/macOS:

cat ~/.ssh/id_ed25519.pub | pbcopy  # macOS
cat ~/.ssh/id_ed25519.pub | xclip -sel clip  # Linux (если установлен xclip)
Windows (Git Bash):

cat ~/.ssh/id_ed25519.pub | clip
Перейдите в настройки GitHub:

Откройте https://github.com/settings/keys.

Нажмите New SSH Key.

Вставьте ключ в поле Key, укажите название (например, "Мой ноутбук") и нажмите Add SSH Key.


3. Клонирование репозитория через SSH
На GitHub откройте нужный репозиторий.

Нажмите Code → SSH и скопируйте ссылку (например, git@github.com:username/repo.git).

В терминале выполните:

git clone git@github.com:username/repo.git
Где username/repo — имя пользователя и репозитория.

Проверка подключения:

ssh -T git@github.com
Если видите Hi username! You've successfully authenticated, всё готово!