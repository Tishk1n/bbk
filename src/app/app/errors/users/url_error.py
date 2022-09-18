class UrlError(Exception):
    def __str__(self) -> str:
        return 'Введите корректную ссылку!'
