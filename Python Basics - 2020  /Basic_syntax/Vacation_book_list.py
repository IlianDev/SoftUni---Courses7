#promenlivi
number_of_pages_per_book = int(input())
pages_per_hour = int (input())
number_of_days_for_book = int (input())

#formuli
full_time_book = number_of_pages_per_book / pages_per_hour
reading_hours_per_day = full_time_book / number_of_days_for_book

print(reading_hours_per_day)
