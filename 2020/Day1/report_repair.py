import sys
sys.path.append("../../")

from lib import utils


def report_repair(expenses):
    expenses = [int(expense) for expense in expenses.splitlines()]
    expenses_set = set(expenses)
    for expense in expenses:
        diff = 2020 - expense
        if diff in expenses_set:
            print(f"Part 1: expense: {expense * diff}")
            break

    for i in range(len(expenses)-3):
        exp_i = expenses[i]
        for j in range(i+1, len(expenses)-2):
            exp_j = expenses[j]
            ij_sum = exp_i + exp_j
            if ij_sum >= 2020:
                continue
            for k in range(j+1, len(expenses)-1):
                if (ij_sum + expenses[k]) == 2020:
                    print(f"Part 2: expense: {exp_i * exp_j * expenses[k]}")
                    break


def problem(expenses):
    report_repair(expenses)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    problem(inp)
