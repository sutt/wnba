#builds small splits of train: 480K record, ~100MB
#note: again training_1 will contain column headers, others will not

n_splits = 10
inp_file = "../data/main/train_10/training_1.csv"
out_file = "../data/main/train_100/training_%d.csv" 

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