from car import Car, Parking


def test():
    parking = Parking()

    samochod1 = Car("RRS-2137X", "red", "car")
    samochod2 = Car("KR-69420", "yellow", "car")

    samochod3 = Car("LBL-39124", "grey", "truck")
    samochod4 = Car("WWA-11111", "transparent", "truck")

    samochod5 = Car("WRO-JW8SB", "beige", "single track")
    samochod6 = Car("RZ-XDXD", "khaki", "single track")

    samochod1.drive_in(parking)
    samochod2.drive_in(parking)
    samochod3.drive_in(parking)
    samochod2.drive_out(parking)

    print("Zajęte miejsca:", parking.occupied_spots)

    samochod2.drive_in(parking)
    samochod4.drive_in(parking)
    samochod5.drive_in(parking)

    print("Zajęte miejsca", parking.occupied_spots, "Utarg:", parking.get_gross_sales())

    samochod6.drive_in(parking)

    samochod1.drive_out(parking)
    samochod6.drive_in(parking)

    print("Zajęte miejsca", parking.occupied_spots, "Utarg:", parking.get_gross_sales())

    # wszystkie samochody out
    parking.empty()

    print("Zajęte miejsca", parking.occupied_spots, "Utarg:", parking.get_gross_sales())

    print(
        "Numery rejestracyjne wszystkich pojazdów:",
        parking.get_car_numbers()
        | parking.get_truck_numbers()
        | parking.get_single_track_numbers(),
    )
    print(
        "Numery rejestracyjne wszystkich pojazdów ciężarowych:",
        parking.get_truck_numbers(),
    )


def main():
    test()


if __name__ == "__main__":
    main()
