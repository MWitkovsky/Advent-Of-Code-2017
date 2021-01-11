import sys
sys.path.append("../../")

import re
from lib import utils


class Passport:
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def __init__(self, passport_str):
        key_value_pairs = re.split("\s+", passport_str)
        self.passport_data = {}
        for pair in key_value_pairs:
            if not pair:
                continue
            pair = pair.split(":")
            self.passport_data[pair[0]] = pair[1]

    @property
    def has_valid_fields(self):
        return all(f in self.passport_data for f in self.required_fields)

    @property
    def is_valid(self):
        try:
            if not 1920 <= int(self.passport_data["byr"]) <= 2002:
                return False

            if not 2010 <= int(self.passport_data["iyr"]) <= 2020:
                return False

            if not 2020 <= int(self.passport_data["eyr"]) <= 2030:
                return False

            if "cm" in self.passport_data["hgt"]:
                height = int(self.passport_data["hgt"][:-2])
                if not 150 <= height <= 193:
                    return False
            elif "in" in self.passport_data["hgt"]:
                height = int(self.passport_data["hgt"][:-2])
                if not 59 <= height <= 76:
                    return False
            else:
                return False

            if not re.match("^#[0-9a-f]{6}$", self.passport_data["hcl"]):
                return False

            if self.passport_data["ecl"] not in self.valid_eye_colors:
                return False

            if not re.match("^[0-9]{9}$", self.passport_data["pid"]):
                return False
        except Exception as ex:
            return False
        return True


def passport_processing(passport_strings):
    passport_strings = passport_strings.split("\n\n")
    passports = [Passport(pp_string) for pp_string in passport_strings]
    print(f"part 1: {sum(pp.has_valid_fields for pp in passports)} passports")
    num_valid = sum(pp.has_valid_fields and pp.is_valid for pp in passports)
    print(f"part 2: {num_valid} passports")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    passport_processing(inp)
