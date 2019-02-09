import csv_manager as csv

[a_user, a_id, a_stars, a_unix_time] = csv.read_data('answer_set.csv')
[t_user, t_id, t_stars, t_unix_time] = csv.read_data('answer_set.csv')

mse = sum((a_stars - t_stars) ** 2)
print('score: ' + str(mse))
