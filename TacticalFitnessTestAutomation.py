# Made by asher-epstein-42
def main():
    while True:
        name = input("name of the tactical athlete: ")
        pullups_final_grade = pullups_grade(int(input("input number of pull ups from 1 to 15: ")))
        dips_final_grade = dips_grade(int(input("input number of dips from 1 to 20: ")))
        xbar_final_grade = xbar_grade(int(input("input number of reps with xbar from 1 to 20: ")))
        sprints_final_grade = sprints_grade(int(input("input sprint time in seconds(for example 53): ")))
        long_run_final_grade = long_run_grade(float(input("input 3 km run time in min.sec (for example 12.34): ")))
        athlete_final_grade = final_grade(pullups_final_grade, dips_final_grade, xbar_final_grade, sprints_final_grade,
                                          long_run_final_grade)
        f = open("TacticalAthletesGrades.txt", "a")  # opens a file and appends to existing content 
        f.write(f"\n{name} -> {athlete_final_grade}")

        f = open("TacticalAthletesGrades.txt", "r")  # displays the file on the screen 
        print(f.read())


def final_grade(pull_ups, dips, x_bar, sprints, long_run):
    return int(pull_ups) * 0.2 + int(dips) * 0.2 + int(x_bar) * 0.2 + float(long_run) * 0.3 + int(
        sprints) * 0.1  # calculating the final grade


def pullups_grade(pull_ups_count):  # min 1 max 15
    pull_up_grades = {1: 35, 2: 40, 3: 45, 4: 45, 5: 50, 6: 55, 7: 60, 8: 65, 9: 70, 10: 75, 11: 80, 12: 85, 13: 90,
                      14: 95, 15: 100}
    return pull_up_grades[pull_ups_count]


def dips_grade(dips_count):  # min 1 max 20
    dips_grades = {1: 35, 2: 40, 3: 45, 4: 45, 5: 55, 6: 58, 7: 61, 8: 64, 9: 67, 10: 70, 11: 73, 12: 76, 13: 79,
                   14: 82, 15: 85, 16: 88, 17: 91, 18: 94, 19: 97, 20: 100}
    return dips_grades[dips_count]


def xbar_grade(xbar_count):  # min 1 max 20
    xbar_grades = {1: 35, 2: 40, 3: 45, 4: 45, 5: 55, 6: 58, 7: 61, 8: 64, 9: 67, 10: 70, 11: 73, 12: 76, 13: 79,
                   14: 82, 15: 85, 16: 88, 17: 91, 18: 94, 19: 97, 20: 100}
    return xbar_grades[xbar_count]


def sprints_grade(sprint_time):
    sprint_grades = {range(0, 41): 100, range(41, 43): 95, range(43, 45): 90, range(45, 47): 85, range(47, 49): 80,
                     range(49, 51): 75, range(51, 53): 70,
                     range(55, 57): 65, range(57, 100): 60}
    for key in sprint_grades:
        if sprint_time in key:
            return sprint_grades[key]


def long_run_grade(run_time):  # 3 km run 
    # list of time ranges. for each range missed one point is comung off
    list_run_grades = [[0, 10.57], [10.56, 11.04], [11.03, 11.10], [11.09, 11.15],
                       [11.14, 11.20], [11.19, 11.25], [11.24, 11.30],
                       [11.29, 11.36],
                       [11.35, 11.40], [11.39, 11.45], [11.44, 11.50], [11.49, 11.56],
                       [11.55, 12.00], [11.59, 12.05], [12.04, 12.10],
                       [12.09, 12.15],
                       [12.14, 12.20], [12.19, 12.26], [12.25, 12.32], [12.31, 12.38],
                       [12.37, 12.44], [12.43, 12.50], [12.49, 12.56], [12.55, 13.02], [13.01, 13.08], [13.07, 13.14],
                       [13.13, 13.20],
                       [13.19, 13.25],
                       [13.24, 13.30], [13.29, 13.35], [13.34, 13.40], [13.39, 13.45], [13.44, 13.50],
                       [13.49, 13.55], [13.54, 14.00], [13.59, 14.05], [14.04, 14.10]]

    for i in range(len(list_run_grades)):
        if list_run_grades[i][0] < run_time < list_run_grades[i][1]:
            return 100 - i  # for each step in the list one point is coming off


if __name__ == '__main__':
    main()
