import sys
sys.path.append("../../")

from lib import utils
from collections import defaultdict, Counter


def repose_record(inp):
    duty_log = inp.splitlines()
    duty_log = sorted(duty_log, key=lambda x: x[:18])

    curr_guardid = None
    sleep_min = None
    guardid_2_num_minutes_slept = defaultdict(int)
    guardid_2_specific_minutes_slept = defaultdict(Counter)
    for log in duty_log:
        if "Guard" in log:
            curr_guardid = int(log[log.index("#")+1:log.index("begins")-1])
        elif "l" in log:
            sleep_min = int(log[15:17])
        elif "w" in log:
            awake_min = int(log[15:17])
            guardid_2_num_minutes_slept[curr_guardid] += awake_min - sleep_min
            for i in range(sleep_min, awake_min, 1):
                guardid_2_specific_minutes_slept[curr_guardid][i] += 1

    most_sleepy_guardid = sorted(guardid_2_num_minutes_slept.keys(),
                                 key=lambda x: guardid_2_num_minutes_slept[x],
                                 reverse=True)[0]

    most_popular_minute = guardid_2_specific_minutes_slept[most_sleepy_guardid].most_common(1)[0][0]

    print ("part 1: {0}".format(most_sleepy_guardid * most_popular_minute))

    most_predictable_guardid = None
    most_probable_minute = None
    for guardid, sleep_minutes in guardid_2_specific_minutes_slept.items():
        guard_most_common_sleep_minute = sleep_minutes.most_common(1)[0]
        if most_predictable_guardid is None or\
                guard_most_common_sleep_minute[1] > most_probable_minute[1]:
            most_predictable_guardid = guardid
            most_probable_minute = guard_most_common_sleep_minute

    print ("part 2: {0}".format(most_predictable_guardid * most_probable_minute[0]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    repose_record(inp)
