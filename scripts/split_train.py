#split train.csv (10GB) into 10 seperate files
# note: training_1 will still have col names, others will not

n_splits = 10
inp_file = "../data/orig/train.csv"
out_file = "../data/main/train_10/training_%d.csv" # %d will be 1,2,,...,n_splits

# open files to write
# save pointers to a list
out_files = []
for n in range(n_splits):
    out_files.append(open(out_file % (n+1),"w"))

with open(inp_file) as f:
    for ind,line in enumerate(f):
        split_id = ind % n_splits # every nth row goes to nth split
        out_files[split_id].write(line)
        
# clean up - close files
for f in out_files:
    f.close()