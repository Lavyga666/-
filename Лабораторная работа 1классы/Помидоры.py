import doctest
class TomatoGrowing:
    """
    Абстрактный класс, описывающий объект выращивания помидоров.
    """

    def __init__(self, tomato_variety: str, ripe_tomatoes_count: int, occupied_area: float):
        """
        Создание и подготовка к выращиванию объекта "TomatoGrowing".

        :param tomato_variety: Сорт помидоров.
        :param ripe_tomatoes_count: Количество зрелых помидоров.
        :param occupied_area: Площадь, занимаемая помидорами.

        Пример:
        >>> tomatoes = TomatoGrowing("Черри", 50, 10.0)
        """
        # Валидация аргументов конструктора
        if not isinstance(tomato_variety, str):
            raise TypeError("Сорт помидоров должен быть строкой")
        self.tomato_variety: str = tomato_variety

        if not isinstance(ripe_tomatoes_count, int) or ripe_tomatoes_count < 0:
            raise ValueError("Количество зрелых помидоров должно быть неотрицательным целым числом")
        self.ripe_tomatoes_count: int = ripe_tomatoes_count

        if not isinstance(occupied_area, (int, float)) or occupied_area <= 0:
            raise ValueError("Площадь, занимаемая помидорами, должна быть положительным числом")
        self.occupied_area: float = occupied_area

    def add_additional_area(self, additional_area: float) -> None:
        """
        Метод, описывающий добавление новой площади для выращивания помидоров.

        :param additional_area: Дополнительная площадь.

        Пример:
        >>> tomatoes = TomatoGrowing("Черри", 50, 10.0)
        >>> tomatoes.add_additional_area(5.0)
        """
        ...

    def harvest_tomatoes(self, harvested_count: int) -> None:
        """
        Метод, описывающий сбор помидоров.

        :param harvested_count: Количество собираемых помидоров.

        Пример:
        >>> tomatoes = TomatoGrowing("Черри", 50, 10.0)
        >>> tomatoes.harvest_tomatoes(10)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
