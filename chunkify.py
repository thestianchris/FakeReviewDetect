import io
import pandas as pd

chunks = pd.read_json('yelp_academic_dataset_review.json', lines=True, chunksize = 50000)
reviews = pd.DataFrame()
for chunk in chunks:
  reviews = pd.concat([reviews, chunk])
  print(reviews.iloc[0].text)
  break


reviews.savetxt(r'50kreview.txt', header=None, index=None, sep=' ')
