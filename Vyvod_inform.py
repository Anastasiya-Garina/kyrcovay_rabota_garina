import datetime
import re

day_d = {0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday", 4: "friday", 5: "saturday"}
week_days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
# Определяем текущую дату
dt_now = datetime.datetime.now()
# День недели
dt_week = dt_now.weekday()
dt_m = dt_now.month
dt_d = dt_now.day

def vxod(schedule_):
    # dt_now.hour, dt_now.minute
    # eval(str_poisk + "[" + str(j) + "].time")[0:2]
    # zapros ="с++ - запрос на расписание по названию предмета"
    # zapros ="улитин - запрос на получение расписания по фамилии преподавателя"
    # zapros ="Запрос на расписание по дню неделю. Код дня недели: 4"
    # zapros ="13 - запрос на получение расписания по дате, ddmm - день сегодня, 1305 - искомая дата"
    zapros ="алгоритмы - запрос на расписание по названию предмета"
    # zapros ="носков - запрос на получение расписания по фамилии преподавателя"

    if zapros.lower().find("по названию предмета".lower()) > 0:
        #Ищем по предмету
        subject = zapros[:zapros.find(" -")]
        poisk_subject(schedule_, subject)
    elif zapros.lower().find("по фамилии преподавателя".lower()) > 0:
        # Ищем по преподавателю
        lector = zapros[:zapros.find(" -")]
        poisk_lector(schedule_,lector)
    elif zapros.lower().find("на расписание по дню неделю".lower()) > 0:
        # Ищем по дню недели
        day_week = int(zapros[-1]) - 1
        poisk_day_week(schedule_, day_week)
    elif zapros.lower().find("на получение расписания по дате".lower()) > 0:
        # Ищем по дате
        data_zapros = zapros[(zapros.find(" - искомая дата") - 4):(zapros.find(" - искомая дата"))]
        zapros_d = int(data_zapros[:2])
        zapros_m = int(data_zapros[2:])
        zapros_y = dt_now.year
        zapros_data = datetime.date(zapros_y, zapros_m, zapros_d)
        zapros_d_w = zapros_data.weekday()
        poisk_data(schedule_, zapros_d_w, zapros_data)

# ищем предмет
def poisk_subject(schedule_, param_):
    for i in range(6):
        str_poisk = "schedule_." + day_d[(dt_week + i) % 6]
        for j in range(len(eval(str_poisk))):
            str_poisk_l = str_poisk + "[" + str(j) + "].lesson_name"
            if eval(str_poisk_l).lower().find(param_.lower()) >= 0:
                print(week_days[(dt_week + i) % 6] + " " + eval(str_poisk + "[" + str(j) + "].time"))
                print(eval(str_poisk_l).replace("\n", " "))
                return
    print("Не найдено")
    return

# ищем преподавателя
def poisk_lector(schedule_, param_):
    for i in range(6):
        str_poisk = "schedule_." + day_d[(dt_week + i) % 6]
        for j in range(len(eval(str_poisk))):
            # str_poisk_l = str_poisk + "." + str(j) + ".lectures"
            str_poisk_l = str_poisk + "[" + str(j) + "].lesson_name"
            if eval(str_poisk_l).lower().find(param_.lower()) > 0:
                print(week_days[(dt_week + i) % 6] + " " + eval(str_poisk + "[" + str(j) + "].time"))
                print(eval(str_poisk_l).replace("\n", " "))
                return
    print("Не найдено")
    return

# ищем по дню недели
def poisk_day_week(schedule_, param_):
    if param_ < 6:
        str_poisk = "schedule_." + day_d[param_]
        if len(eval(str_poisk)) > 0:
            str_rez = week_days[param_] + "\n"
            for j in range(len(eval(str_poisk))):
                str_rez += str(j + 1) + " " + eval(str_poisk + "[" + str(j) + "].time") + " " + \
                           eval(str_poisk + "[" + str(j) + "].lesson_name").replace("\n", ' ') + "\n"
            print(str_rez)
        else:
            print("Не учебный день")
    else:
        print("Не учебный день")
    return

# Ищем по дате
def poisk_data(schedule_, d_n, data_z):
    if d_n < 6:
        str_poisk = "schedule_." + day_d[d_n]
        if len(eval(str_poisk)) > 0:
            str_rez = data_z.strftime('%d.%m.%y') + " " + week_days[d_n] + "\n"
            for j in range(len(eval(str_poisk))):
                str_rez += str(j + 1) + " " + eval(str_poisk + "[" + str(j) + "].time") + " " + \
                           eval(str_poisk + "[" + str(j) + "].lesson_name").replace("\n", ' ') + "\n"
            print(str_rez)
        else:
            print("Не учебный день")
    else:
        print("Не учебный день")
    return