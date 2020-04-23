from TourCard import TourCard


def main():
    egypt = TourCard("Egypt", 10, 4800, 100, "Oleh", "CoralSea")
    texas = TourCard("Texas", 7, 11000, 40, "Anna", "Carparos")
    lasVegas = TourCard("LasVegas", 5, 120000, 25, "Elina", "Vintage")
    print(egypt.__str__())
    print(texas.__str__())
    print(lasVegas.__str__())


if __name__ == "__main__":
    main()
