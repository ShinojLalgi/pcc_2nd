def describe_city(city, country = 'india'):
    """ Describes a city in a country """
    print(f"{city.title()} is in {country.title()}.")

describe_city('mumbai')
describe_city('delhi')
describe_city('sydney', 'australia')