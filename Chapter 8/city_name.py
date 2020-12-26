def city_country(city, country):
    """ Returns a formatted string """
    
    return f"{city.title()}, {country.title()}"

print(city_country('mumbai', 'india'))
print(city_country('delhi', 'india'))
print(city_country('sydney', 'australia'))