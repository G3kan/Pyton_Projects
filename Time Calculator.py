def add_time(start, duration, day=None):
    
    start_time, pr = start.split()
    start_cl, start_minu = start_time.split(":")
    start_cl, start_minu = int(start_cl), int(start_minu)
    
    if pr == "PM" and start_cl != 12:
        start_cl += 12

    duration_h, duration_min = map(int, duration.split(":"))

    if duration_min > 59:
        return "Error"

    new_h = start_cl + duration_h
    new_minu = start_minu + duration_min

    new_h += new_minu // 60
    new_minu %= 60
    
    days_passed = new_h // 24
    new_h %= 24

    if new_h < 12:
        new_p = "AM"
    else:
        new_p = "PM"
    
    new_h %= 12
    
    if new_h == 0:
        new_h = 12

    new_time = f"{new_h}:{new_minu:02d} {new_p}"

    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day:
        day = day.capitalize()
        day_index = week_list.index(day)
        next_day_index = (day_index + days_passed) % 7
        new_time += f", {week_list[next_day_index]}"


    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"


    return new_time

