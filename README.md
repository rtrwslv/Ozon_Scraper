ОПИСАНИЕ К ПРОЕКТУ:
1. create_assistant.py - файл автоматизации для создания ассистента(в проекте напрямую не используется, оставлен на всякий случай)
2. mail_parser.py - файл в котором содержится метод, который парсит код из почты
3. request_sender.py - файл, который отсылает запрос к ChatGPT и возвращает ответ от нейросети
4. response_to_reviews - файл, который отвечает на рецензии пользователей
5. review_scraper - файл, который заходит в лк Ozon и парсит отзывы

ПОРЯДОК ЗАПУСКА:
Необходимо обновить Google Chrome до последней версии!

pip install requirements.txt
python3 review_scraper.py(На этом моменте лучше всего не использовать VPN, так как cloudfare и Ozon блокируют подключение с их публичного IP)
python3 response_to_reviews.py(Перед запуском необходимо использовать VPN, так как OpenAI блокирует российские IP адреса)
Результат выполнения хранится в файле responses.txt