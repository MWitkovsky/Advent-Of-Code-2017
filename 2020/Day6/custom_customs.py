import sys
sys.path.append("../../")

from lib import utils  # noqa: E402


class CustomsGroup:
    def __init__(self, group_answers):
        self.group_answers = group_answers
        self.any_yes_set = set()
        self.all_yes_set = None
        member_answers = group_answers.split("\n")
        for answers in member_answers:
            self.any_yes_set.update(answers)
            if self.all_yes_set is None:
                self.all_yes_set = set(answers)
            else:
                self.all_yes_set -= self.all_yes_set - set(answers)

    @property
    def num_any_yes(self):
        return len(self.any_yes_set)

    @property
    def num_all_yes(self):
        return len(self.all_yes_set)


def custom_customs(customs_strings):
    customs_strings = customs_strings.split("\n\n")
    customs_groups = \
        [CustomsGroup(customs_string) for customs_string in customs_strings]
    print(f"Part 1: {sum(group.num_any_yes for group in customs_groups)}")
    print(f"Part 2: {sum(group.num_all_yes for group in customs_groups)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    custom_customs(inp)
