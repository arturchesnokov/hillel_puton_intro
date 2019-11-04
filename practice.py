# передаем список строк из файла, и названия параметров для группировки
def aggregate_values_by_group(source, value_name, group_name):
    # получаем индекс по названию параметра
    value_index = source[0].split(",").index(value_name)
    group_index = source[0].split(",").index(group_name)
    dictionary = {}

    for line in source[1:]:
        if line:
            splitted_string = line.split(",")
            group = splitted_string[group_index]
            value = float(splitted_string[value_index])

            if group in dictionary:
                dictionary[group] += value
            else:
                dictionary[group] = value

    return dictionary


# надеюсь правильно понял задание и нужно в рамках региона разбить профит по странам
def aggregate_values_by_group_subgroup(source, value_name, group_name, subgroup_name):
    # получаем индекс по названию параметра
    value_index = source[0].split(",").index(value_name)
    group_index = source[0].split(",").index(group_name)
    subgroup_index = source[0].split(",").index(subgroup_name)
    dictionary = {}

    for line in source[1:]:
        if line:
            splitted_string = line.split(",")
            group = splitted_string[group_index]
            subgroup = splitted_string[subgroup_index]
            value = float(splitted_string[value_index])

            if group in dictionary:
                if subgroup in dictionary[group]:
                    dictionary[group][subgroup] += value
                else:
                    dictionary[group][subgroup] = value
            else:
                dictionary[group] = {subgroup: value}

    return dictionary


# печатаем N значений словаря в обратном порядке (по значению)
def print_dict_by_value_reversed(d, N):
    for pair in sorted(d.items(), key=lambda v: v[1], reverse=True)[:N]:
        print(pair[0], pair[1])


# печатаем весь двухуровневый словарь
def print_dict(d):
    for pair in sorted(d.items()):
        print(pair[0], end=":\n")
        for val in sorted(pair[1].items()):
            print("\t", val[0], val[1])


# Region,Country,Item Type,Sales Channel,Order Priority,
# Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit

# можно передавать в функцию просто название файла, но тогда нужно будет каждый раз открывать/читать /закрывать
file = open("500000_records.csv")
data_source = file.read().split("\n")
file.close()

# формируем словари по нужным нам критериям
profit_by_country = aggregate_values_by_group(data_source, "Total Profit", "Country")
revenue_by_country = aggregate_values_by_group(data_source, "Total Revenue", "Country")
revenue_by_channel = aggregate_values_by_group(data_source, "Total Revenue", "Sales Channel")
profit_by_region_country = aggregate_values_by_group_subgroup(data_source, "Total Profit", "Region", "Country")

print("\n1. Top 10 countries by profit:")
print_dict_by_value_reversed(profit_by_country, 10)

print("\n2. Top 10 countries by revenue:")
print_dict_by_value_reversed(revenue_by_country, 10)

print("\n4. Top 5 channels by revenue:")
print_dict_by_value_reversed(revenue_by_channel, 5)

print("\n3. Profit by Region - Country:")  # Да, не по порядку, но такой большой список специально вынес
print_dict(profit_by_region_country)
