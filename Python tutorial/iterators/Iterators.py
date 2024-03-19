def main():
    countries = ("Germany", "France", "Italy", "Spain")
    print(type(countries))
    country_iter = iter(countries)
    # iterable
    print(next(country_iter))
    iter_copy = iter(country_iter)
    print(next(iter_copy))
    # iterator
    country_iter2 = iter(countries)
    print(next(country_iter2))

    for country in countries:
        print(country)

    with open("countries.txt") as file:
        for line in iter(file.readline, ""):
            print(line, end="")


if __name__ == "__main__":
    main()
