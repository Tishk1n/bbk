def convert_from_dict_to_str(user_id, data: dict) -> str:
    from_ = __data_from_to_str(data["source"])
    return f'{user_id}:\nОткуда узнал: {from_}\nСсылка: {data["url"]}\nПричина перехода: {data["why"]}'


def __data_from_to_str(data: str) -> str:
    match data:
        case 'lolz':
            return "Лолз"
        case 'advertisement':
            return 'Реклама'
        case 'friend':
            return 'От друга'
        case _:
            return 'Другое'
