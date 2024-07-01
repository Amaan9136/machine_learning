from tqdm import tqdm

count = 0
for i in tqdm(range(1000000)):
  count+=1

print(count)