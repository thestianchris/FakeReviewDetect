import io
import ijson
import pandas as pd

chunks = pd.read_json('yelp_academic_dataset_review.json', lines=True, chunksize = 20000)
reviews = pd.DataFrame()
for chunk in chunks:
  reviews = pd.concat([reviews, chunk])
  print(reviews.iloc[0].text)
  break

