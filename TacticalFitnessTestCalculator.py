from consts import header, pull_up_grades, dips_grades, xbar_grades, sprint_grades, list_run_grades


def main():
    try:
        while True:
            print_header()
            print("Press X to exit")
            name = input("name of the tactical athlete: ")
            if name.lower() in ['x', 'exit']:
                exit_program()
            pullups_final_grade = pullups_grade(int(input("input number of pull ups from 1 to 15: ")))
            dips_final_grade = dips_grade(int(input("input number of dips from 1 to 20: ")))
            xbar_final_grade = xbar_grade(int(input("input number of reps with xbar from 1 to 20: ")))
            sprints_final_grade = sprints_grade(int(input("input sprint time in seconds(for example 53): ")))
            long_run_final_grade = long_run_grade(float(input("input 3 km run time in min.sec (for example 12.34): ")))
            athlete_final_grade = final_grade(pullups_final_grade, dips_final_grade, xbar_final_grade,
                                              sprints_final_grade,
                                              long_run_final_grade)
            write_file(name, athlete_final_grade)
            read_file()
    except KeyboardInterrupt:
        return


def write_file(name: str, final_grade: float):
    f = open("TacticalAthletesGrades.txt", "a")  # opens a file and appends to existing content
    f.write(f"\n{name} -> {final_grade}")


def read_file():
    f = open("TacticalAthletesGrades.txt", "r")  # displays the file on the screen
    print(f.read())


def exit_program():
    print("goodbye!")
    raise KeyboardInterrupt


def print_header():
    print(header)


def final_grade(pull_ups, dips, x_bar, sprints, long_run):
    return int(pull_ups) * 0.2 + int(dips) * 0.2 + int(x_bar) * 0.2 + float(long_run) * 0.3 + int(
        sprints) * 0.1  # calculating the final grade


def pullups_grade(pull_ups_count):  # min 1 max 15
    return pull_up_grades[pull_ups_count]


def dips_grade(dips_count):  # min 1 max 20
    return dips_grades[dips_count]


def xbar_grade(xbar_count):  # min 1 max 20
    return xbar_grades[xbar_count]


def sprints_grade(sprint_time):
    for key in sprint_grades:
        if sprint_time in key:
            return sprint_grades[key]


def long_run_grade(run_time):  # 3 km run 
    # in  list of time ranges, for each range missed one point is coming off
    for i in range(len(list_run_grades)):
        if list_run_grades[i][0] < run_time < list_run_grades[i][1]:
            return 100 - i  # for each step in the list one point is coming off


if __name__ == '__main__':
    main()
