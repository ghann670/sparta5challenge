# Google 인증 (Google Colab에서 실행하는 경우, 인증 절차가 자동으로 진행됩니다)
from google.colab import auth
from google.cloud import bigquery
from google.cloud.exceptions import NotFound


auth.authenticate_user()
# 여기서 YOUR_PROJECT_ID를 Google Cloud 프로젝트 ID로 교체하세요.
project_id = 'practice-250120'
client = bigquery.Client(project=project_id)


# DataFrame을 BigQuery로 업로드
# 여기서 YOUR_DATASET_NAME과 YOUR_TABLE_NAME을 실제 데이터셋 및 테이블 이름으로 교체
dataset_id = 'mydataset'
table_id = 'classicalmusic'

# 데이터셋의 전체 ID. 예: 'your-project.your_dataset'
full_dataset_id = "{}.{}".format(client.project, dataset_id)

# 데이터셋 존재 여부 확인
try:
    client.get_dataset(full_dataset_id)  # API 요청
    print("Dataset {} already exists".format(full_dataset_id))
except NotFound:
    # 데이터셋이 없을 경우, 데이터셋 생성
    dataset = bigquery.Dataset(full_dataset_id)
    dataset.location = "asia-northeast3"
    dataset = client.create_dataset(dataset)  # API 요청
    print("Dataset {} created".format(full_dataset_id))


table_ref = client.dataset(dataset_id).table(table_id)

job = client.load_table_from_dataframe(classicalmusic, f'{dataset_id}.{table_id}')

# 잡이 완료될 때까지 기다립니다.
job.result()

print("업로드 완료")

