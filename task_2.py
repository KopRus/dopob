# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    first = set(group1.split(delimiter))
    second = set(group2.split(delimiter))
    common_participants = first.intersection(second)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print (common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой

