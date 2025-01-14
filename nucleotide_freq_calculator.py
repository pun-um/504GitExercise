#function1 takes a string of nucleotides and makes a dictionary with each base and its number of appearances in the string counted
def function1(nuc_string):
    base_dict = dict()
    for nuc in nuc_string:
        if nuc not in base_dict:
            base_dict[nuc] = 1
        else:
            base_dict[nuc] += 1
    return base_dict

# creates and prints frequencies of letters in a dictionary, given a dictionary
def function2(bp_count_dict):
    print('freqs')
    total = float(sum([bp_count_dict[bp] for bp in bp_count_dict.keys()]))
    for bp in bp_count_dict.keys():
        print(bp + ':' + str(bp_count_dict[bp]/total))

function2(function1('ATCTGACGCGCGCCGC'))
