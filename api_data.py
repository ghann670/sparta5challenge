import requests
import pandas as pd

url = 'https://api.openopus.org/dyn/work/random'
params = {'popularwork': '1',
          'recommendedwork': '1',
          'popularcomposer': '1',
          'epoch': 'Romantic'}

response = requests.post(url, params=params)
data = response.json()
works = data.get('works', [])
df = pd.DataFrame(works)

# composer 컬럼은 딕셔너리 형태로 id, 출생/사망년도 등 다양한 정보를 포함하고 있어서 이름만 추출
df['composer'] = df['composer'].apply(lambda x: x.get('complete_name'))

df.to_csv('classicalmusic.csv', index = False)
classicalmusic = pd.read_csv('classicalmusic.csv')


