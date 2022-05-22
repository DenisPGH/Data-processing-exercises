with open('file_a.csv', 'r') as fa, open('file_b.csv', 'r') as fb:
    fileone_set = set(fa.readlines())
    filetwo_set = set(fb.readlines())

print(fileone_set.symmetric_difference(filetwo_set))


