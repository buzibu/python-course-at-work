academical = int(input("Въведете брой академични часове: "))

# An astronomical hour consists of 60 minutes
# An academical hour consists of 40 minutes
# For each 4 academical hours there are 20 minutes brake

astronomical = (academical*40 + (academical/4)*20)/60

print('{} академични часове са {} астрономически часа'.format(academical,astronomical))