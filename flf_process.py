from fractions import gcd
from sys import exit, stderr

VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvwxz"


class FunLearningFactor(object):
    def __init__(self, tutors_file, players_file):
        self.flf_matrix = []

        # Populate tutor dict.
        # index => {name, len, odd}
        self.t_dict = {}
        with open(tutors_file, 'r') as tf:
            for i, tutor in enumerate(tf.readlines()):
                tutor = tutor.strip()
                self.t_dict[i] = {'name': tutor, 'len': len(tutor),
                    'odd': True if len(tutor) % 2 != 0 else False}

        # Populate player dict.
        # index => {name, len, num_vowels, num_consonants}
        self.p_dict = {}
        with open(players_file, 'r') as pf:
            for i, player in enumerate(pf.readlines()):
                player = player.strip()
                vowels = sum(player.lower().count(ch) for ch in VOWELS)
                consonants = sum(player.lower().count(ch) for ch in CONSONANTS)
                self.p_dict[i] = {'name': player, 'len': len(player),
                                  'num_vowels': vowels,
                                  'num_consonants': consonants}

        # Do we have an equal number of tutors and players?
        t_len = len(self.t_dict)
        p_len = len(self.p_dict)
        if t_len != p_len:
            print >> stderr, "Not an equal number of tutors and players."
            print >> stderr, "Tutors: %d, Players: %d" % (t_len, p_len)
            exit(1)

    def fill_flf_matrix(self):
        """Compute flf of tutor-player pairs and insert into a matrix."""

        for t_itor in xrange(len(self.t_dict)):  # Iterate tutors.
            matrix_row = []
            for p_itor in xrange(len(self.p_dict)):  # Iterate players.
                # Computer flf between a tutor and a player.
                flf = self.calc_flf(self.t_dict[t_itor], self.p_dict[p_itor])
                matrix_row.append(flf)
            self.flf_matrix.append(matrix_row)

    def calc_flf(self, tutor, player):
        """Calculates flf of a tutor-player pair."""

        flf = None

        if tutor['odd']:
            flf = player['num_vowels'] * 1.5
        else:
            flf = player['num_consonants'] * 1.0

        # Check for common factors other than 1.
        if gcd(tutor['len'], player['len']) > 1:
            flf = flf + (flf * 0.5)

        return flf

    def print_flf_matrix(self, msg=None):
        """Return a string representation of the flf matrix."""

        matrix_str = '\n'
        if msg:
            matrix_str += msg + '\n'

        matrix_dim = len(self.t_dict)

        # Print out the vertical line for matrix.
        matrix_str += matrix_dim * '--' + '-\n'

        for row in xrange(matrix_dim):
            matrix_str += '|'
            for col in xrange(matrix_dim):
                matrix_str += str(self.flf_matrix[row][col]) + '|'
            matrix_str += '\n'

        # Print out the vertical line for matrix.
        matrix_str += matrix_dim * '--' + '-\n'

        return matrix_str

    def get_tutor_player_names(self, tutor, player):
        """Given a tutor and player index, return associated names."""

        return '(%s, %s)' % (self.t_dict[tutor]['name'],
                             self.p_dict[player]['name'])
