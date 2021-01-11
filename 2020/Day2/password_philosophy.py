import sys
sys.path.append("../../")

from lib import utils


class ValidatedPassword:
    def __init__(self, rule, password):
        self.password = password
        rule = rule.split(" ")
        rule_range = rule[0].split("-")
        self.target_char = rule[1]
        self.lo = int(rule_range[0])
        self.hi = int(rule_range[1])

    @property
    def is_count_valid(self):
        return self.hi >= self.password.count(self.target_char) >= self.lo

    @property
    def is_position_valid(self):
        lo_match = self.password[self.lo-1] == self.target_char
        hi_match = self.password[self.hi-1] == self.target_char
        return (lo_match or hi_match) and not (lo_match and hi_match)


def password_philosophy(passwords):
    validated_passwords = []
    for password_info in passwords.splitlines():
        rule, password = password_info.split(": ")
        validated_passwords.append(ValidatedPassword(rule, password))

    num_count_valid_passwords = \
        sum(pw.is_count_valid for pw in validated_passwords)
    print(f"Part 1: {num_count_valid_passwords}")
    num_position_valid_passwords = \
        sum(pw.is_position_valid for pw in validated_passwords)
    print(f"Part 2: {num_position_valid_passwords}")


def problem(passwords):
    password_philosophy(passwords)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    problem(inp)
