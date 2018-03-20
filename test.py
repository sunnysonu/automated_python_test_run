import all_test_runs
import glob

def get_submitted_folders(path):
    folders = []
    for item in glob.glob("smec_*"):
        if("." not in item):
            folders.append(item)
    return folders

def run_all_tests(folders):
    scores = []
    for package in folders:
        score = []
        score.append(all_test_runs.test_right_rotations(package))
        score.append(all_test_runs.test_custom_base5(package))
        score.append(all_test_runs.test_top_chars(package))
        score.append(all_test_runs.test_factorize_number(package))
        score.append(all_test_runs.test_get_lcm(package))
        score.append(all_test_runs.test_get_hcf(package))
        score.append(all_test_runs.test_top_earners(package))
        scores.append(score)
    return scores

def get_names(folders):
    names = []
    for folder in folders:
        name = ""
        index = 5
        while(folder[index] != "_"):
            name += folder[index]
            index += 1
        names.append(name)
    return names

def main():
    folders = get_submitted_folders(r"D:\smec_mock1\Unit-Testing-master")
    names = get_names(folders)
    scores = run_all_tests(folders)
    add_content_to_file(names, scores)

def add_content_to_file(name, scores):
    f = open("leaderboard.csv", "w")
    f.write("Name,get_right_rotations,custom_base5,top_chars,factorize,get_lcm,gethcf,top_earners,Total\n")
    totals = [sum(x) for x in scores]
    data = list(zip(name, scores, totals))
    data.sort(key = lambda x : (-x[2], x[0]))
    for row in data:
        print(row)
        f.write(row[0] + ",")
        for score in row[1]:
            f.write(str(score) + ",")
        f.write(str(row[2]) + "\n")
    f.close()

main()