'''
Martin Halvorson

Takes input of switched lines in a sorting network
Boolean output of whether or not the sorting network is valid for all input
'''

def is_valid_sorting_network(input_list = []):

    # Option for manual input if none provided
    if input_list == []:
        newline = input()
        while newline != "":
            input_list.append(tuple(newline.split(' ')))
            newline = input()

    # Change this to reflect however many bits are being represented
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        seq = [a, b, c, d, e] # This changes too based on bits

                        # Represents the comparator
                        for line in input_list:
                            seq[int(line[0])] = min(seq[int(line[0])], seq[int(line[1])])
                            seq[int(line[1])] = max(seq[int(line[0])], seq[int(line[1])])

                        # Sorts seq to check if network sorted the inputs correctly for this combination
                        sorted_seq = sorted(seq)
                        
                        print(str(seq) + "  =>  " + str(seq) + " ~~~ " + str(sorted_seq == seq))


is_valid_sorting_network([(0, 1), (3, 4), (0, 2), (1, 2), (0, 3), (2, 3), (1, 4), (1, 2), (3, 4)])
        
