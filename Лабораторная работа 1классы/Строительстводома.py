import doctest
class HouseConstruction(ABC):
    """
    Абстрактный класс, описывающий объект строительства дома.
    """
    def __init__(self, num_floors: int, total_area: float):
        """
        Создание объекта строительства дома с указанным количеством этажей и общей площадью.

        :param num_floors: Количество этажей в доме.
        :param total_area: Общая площадь дома.

        Пример:
        >>> house = HouseConstruction(2, 150.0)
        """
        if not isinstance(num_floors, int) or num_floors <= 0:
            raise ValueError("Количество этажей должно быть положительным целым числом")
        self.num_floors: int = num_floors

        if not isinstance(total_area, (int, float)) or total_area <= 0:
            raise ValueError("Общая площадь должна быть положительным числом")
        self.total_area: float = total_area


    def add_balcony(self, balcony_area: float) -> None:
        """
        Метод описывающий добавление новой площади путем пристройки балкона.

        :param balcony_area: Площадь балкона, которую необходимо добавить.

        Пример:
        >>> house.add_balcony(10.0)
        """
        ...

    def add_floor(self, additional_floors: int) -> None:
        """
        Метод описывающий добавление нового этажа.

        :param additional_floors: Количество новых этажей.

        Пример:
        >>> house.add_floor(1)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
