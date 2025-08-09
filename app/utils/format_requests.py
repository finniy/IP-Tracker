from app.messages.message_text import NO_HISTORY_TEXT

def format_user_requests(requests: list, username: str) -> str:
    # Формирует строку с пронумерованным списком запросов для отправки одним сообщением
    if not requests:
        return NO_HISTORY_TEXT.format(username)

    lines = [f"{i}. {req}" for i, req in enumerate(requests, start=1)]
    return f"История запросов {username}:\n" + "\n".join(lines)
