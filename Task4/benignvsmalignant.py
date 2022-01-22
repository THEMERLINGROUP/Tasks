from itertools import groupby
benign_tumors_perimeter_mean_over_80mm = [{'id':867387, 'Size':102}, {'id':866458, 'Size':99.58}, {'id':86561, 'Size':88.44}, {'id':865468, 'Size':86.1}, {'id':865432, 'Size':94.28}, {'id':86409, 'Size':97.83}, {'id':86408, 'Size':82.15}, {'id':862009, 'Size':86.6}, {'id':861853, 'Size':84.74}, {'id':861648, 'Size':94.57}, {'id':861598, 'Size':95.77},
{'id':8611161, 'Size':86.49}, {'id':8610908, 'Size':83.19}, {'id':8610629, 'Size':87.91}, {'id':859487, 'Size':81.37}, {'id':857810, 'Size':82.61}, {'id':857373, 'Size':87.21}, {'id':857156, 'Size':86.91}, {'id':854941, 'Size':82.61}, {'id':8510653, 'Size':85.63}, {'id':8510426, 'Size':87.46}, {'id':893526, 'Size':85.69}, {'id':893548, 'Size':82.71}, {'id':89382601, 'Size':92.68}]
benign_grp = groupby(benign_tumors_perimeter_mean_over_80mm, key=lambda x:x['Size'])
for key, value in benign_grp:
    print(key, list(value))
    
malignant_tumors_under_80mm_perimeter = [{'id':9013838, 'Size':73.3}, {'id':869691, 'Size':78.99}, {'id':855563, 'Size':71.9}, {'id':853612, 'Size':77.93}, {'id':84348301, 'Size':77.58}]
malignant_grp = groupby(malignant_tumors_under_80mm_perimeter, key=lambda x:x['Size'])
for key, value in malignant_grp:
    print(key, list(value))
largest_benign_tumors = [{'id':8915, 'Size':97.03}, {'id':915452, 'Size':104.7}]
largest_concavity_means = [{'id':926125, 'Concavity':0.3174}, {'id':925622, 'Concavity':0.255}, {'id':91485, 'Concavity':0.2188}, {'id':9113538, 'Concavity':0.2136}, {'id':'911296202', 'Concavity':0.3635}, {'id':907914, 'Concavity':0.2733}, {'id':90439701, 'Concavity':0.3189}, {'id':903516, 'Concavity':0.281}, {'id':899987, 'Concavity':0.3368}, {'id':899667, 'Concavity':0.2914}, {'id':89812, 'Concavity':0.2308}, {'id':89263202, 'Concavity':0.2283}, {'id':8912280, 'Concavity':0.1948}, {'id':8910988, 'Concavity':0.2195}, {'id':887181, 'Concavity':0.3176}, {'id':886776, 'Concavity':0.2448}, {'id':884948, 'Concavity':0.2712}, {'id':881972, 'Concavity':0.191}, {'id':8810703, 'Concavity':0.3201}, {'id':878796, 'Concavity':0.3523}, {'id':87164, 'Concavity':0.2032}, {'id':863030, 'Concavity':0.2071}, {'id':8610862, 'Concavity':0.3754}, {'id':85382601, 'Concavity':0.2417}, {'id':84348301, 'Concavity':0.2414}]
concavity_grp = groupby(largest_concavity_means, key=lambda x:x['Concavity'])
for key, value in concavity_grp:
    print(key, list(value))
largest_benign_concavities = [{'id':86409, 'Concavity':0.3003}, {'id':8710441, 'Concavity':0.4108}]