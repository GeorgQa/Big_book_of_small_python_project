

def printing_for_interview(company:str ="Ozon") -> str:
    if not isinstance(company, str):
        raise TypeError("company должен быть строкой")

    string_name = f"Я смотрю собеседование в компанию {company}"
    print(string_name)


printing_for_interview(company=None)