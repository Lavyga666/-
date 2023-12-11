import doctest
class HouseConstruction:
    """
    Абстрактный класс, описывающий объект строительства дома.
    """
    def __init__(self, floors: int, total_area: float):
        """
        Создание и подготовка к работе объекта строительства дома.

        :param floors: Количество этажей.
        :param total_area: Общая площадь дома.

        Пример:
        >>> house = HouseConstruction(2, 150.5)
        """
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Количество этажей должно быть положительным целым числом")
        self.floors: int = floors

        if not isinstance(total_area, (int, float)) or total_area <= 0:
            raise ValueError("Общая площадь дома должна быть положительным числом")
        self.total_area: float = total_area

    def add_balcony_extension(self, additional_area: float) -> None:
        """
        Метод описывающий добавление новой площади путем пристройки балкона.

        :param additional_area: Дополнительная площадь, добавляемая балконом.
        :return: None
        """
        ...

    def add_new_floor(self) -> None:
        """
        Метод описывающий добавление нового этажа.

        :return: None
        """
        ...
if __name__ == "__main__":
    doctest.testmod()