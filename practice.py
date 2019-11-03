data_source = open("1000_records.csv").read().split("\n")

profit_by_country = {}

for line in data_source[1:]:
    # print(line)
    if line:
        splitted_string = line.split(",")
        country = splitted_string[1]
        profit = float(splitted_string[-1])

        if country in profit_by_country:
            profit_by_country[country] = profit_by_country.get(country) + profit
        else:
            profit_by_country[country] = profit

for line in sorted(profit_by_country.items(), key=lambda val: val[1]):
    print(line[0], line[1])
