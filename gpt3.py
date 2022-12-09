import os
import openai
import pandas as pd
openai.api_key = "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"

df = []
df = pd.DataFrame(df)

for i in range(2):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Create 5 lengthy negative reviews that could be found on tripadvisor for a hotel or restaurant",
        temperature=1.2,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=1.44,
        presence_penalty=0.87
    )
    res = response.choices[0].text.lstrip(' ')
    res = res.split("\n")
    #df2 = pd.DataFrame([[res]],
    #             columns=['review'])
    #df = pd.concat([df,df2])
    
df = pd.DataFrame(df)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
   print(df)
df.to_csv('reviews_generated.csv', mode='a', header=False,index=False)






