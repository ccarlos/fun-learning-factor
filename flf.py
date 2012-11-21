from sys import argv, exit, stderr

from flf_process import FunLearningFactor


def main(argv):
    if len(argv) != 2:
        print >> stderr, "Insufficient number of arguments."
        print >> stderr, "Usage: flf.py tutors players"
        exit(2)

    tutors_file = argv[0]
    players_file = argv[1]

    flf = FunLearningFactor(tutors_file, players_file)
    flf.fill_flf_matrix()
    print flf.print_flf_matrix()


if __name__ == '__main__':
    exit(main(argv[1:]))
