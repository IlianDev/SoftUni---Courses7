countries = input().split(", ")
capitals = input().split(", ")

result = {country: capital for country, capital in zip(countries, capitals)}
for key, value in result.items():
    print(f"{key} -> {value}")
