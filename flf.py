from sys import argv, exit, stderr

from munkres.munkres import Munkres, make_cost_matrix
from flf_process import FunLearningFactor

# Assuming a flf cannot be greater than 1 million.
HIGH_FLOAT = 1000000.0


def main(argv):
    """
    Usage: python flf.py tutors players

    See README for problem description.
    """

    if len(argv) != 2:
        print >> stderr, "Insufficient number of arguments."
        print >> stderr, "Usage: flf.py tutors players"
        exit(2)

    tutors_file = argv[0]
    players_file = argv[1]

    # Find tutor-player matches that yield the highest flf.
    flf = FunLearningFactor(tutors_file, players_file)
    flf.fill_flf_matrix()

    # Use lambda since we want to calculate the maximum instead of a
    # mininum, using Munkres algorithm.
    cost_matrix = make_cost_matrix(flf.flf_matrix,
                                   lambda cost: HIGH_FLOAT - cost)

    m = Munkres()
    indeces = m.compute(cost_matrix)
    print flf.print_flf_matrix(msg='Tutor-Player flf matrix:')

    # Calculate highest yielding tutor-player pairs and total flf.
    total = 0.0
    print 'Highest yielding pairs (tutor, player):'
    for row, col in indeces:
        value = flf.flf_matrix[row][col]
        total = total + value
        print '(%d, %d) -> %f, %s' % (row, col, value,
            flf.get_tutor_player_names(row, col))
    print 'total flf = %f\n' % total


if __name__ == '__main__':
    exit(main(argv[1:]))
