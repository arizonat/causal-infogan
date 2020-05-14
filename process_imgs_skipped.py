import pickle

new_dir = '/home/cail/Documents/causal-infogan/'
old_dir = '/home/thanard/Downloads/'
filename = "imgs_skipped_1.pkl"

f = open(filename,"rb")
hs = pickle.load(f)

nhs = []

for h in hs:
    k = ((h[0][0].replace(old_dir,new_dir),h[0][1]),(h[1][0].replace(old_dir, new_dir),h[1][1]))
    nhs.append(k)
f.close()

with open(filename,"wb") as f:
    pickle.dump(nhs, f)
