from sys import argv, exit, stderr


VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvwxz"


def main(argv):
    if len(argv) != 2:
        print >> stderr, "Insufficient number of arguments."
        print >> stderr, "Usage: flf.py tutors players"
        exit(2)

    tutors_file = argv[0]
    players_file = argv[1]

    # Populate tutor dict.
    t_dict = {}
    with open(tutors_file, 'r') as tf:
        for i, tutor in enumerate(tf.readlines()):
            tutor = tutor.strip()
            t_dict[i] = {'name': tutor, 'len': len(tutor),
                         'odd': True if len(tutor) % 2 != 0 else False}

    # Populate player dict.
    p_dict = {}
    with open(players_file, 'r') as pf:
        for i, player in enumerate(pf.readlines()):
            player = player.strip()
            vowels = sum(player.lower().count(ch) for ch in VOWELS)
            consonants = sum(player.lower().count(ch) for ch in CONSONANTS)
            p_dict[i] = {'name': player, 'len': len(player),
                         'num_vowels': vowels, 'num_consonants': consonants}

    # Do we have an equal number of tutors and players?
    t_len = len(t_dict)
    p_len = len(p_dict)
    if t_len != p_len:
        print >> stderr, "There is not and equal number of tutors and players."
        print >> stderr, "Tutors: %d, Players: %d" % (t_len, p_len)
        exit(2)  # TODO: look up proper exit code


if __name__ == '__main__':
    exit(main(argv[1:]))
