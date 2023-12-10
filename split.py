import os
import random
import shutil

def split_data(source_folder, train_ratio=0.7, validation_ratio=0.1, test_ratio=0.2, seed=None):
    # 폴더 내의 파일 목록을 가져오기
    file_list = os.listdir(source_folder)
    
    # 파일을 섞기 위해 시드(seed) 설정
    if seed:
        random.seed(seed)
    
    # 파일을 무작위로 섞기
    random.shuffle(file_list)
    
    # 데이터를 나누기
    total_files = len(file_list)
    train_split = int(train_ratio * total_files)
    validation_split = int(validation_ratio * total_files)
    
    train_files = file_list[:train_split]
    validation_files = file_list[train_split:train_split + validation_split]
    test_files = file_list[train_split + validation_split:]
    
    # 나눈 데이터를 저장할 폴더 생성
    train_folder = os.path.join(source_folder, 'train')
    validation_folder = os.path.join(source_folder, 'validation')
    test_folder = os.path.join(source_folder, 'test')
    
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    
    # 데이터를 각 폴더로 복사
    for file in train_files:
        shutil.copy(os.path.join(source_folder, file), os.path.join(train_folder, file))
    
    for file in validation_files:
        shutil.copy(os.path.join(source_folder, file), os.path.join(validation_folder, file))
    
    for file in test_files:
        shutil.copy(os.path.join(source_folder, file), os.path.join(test_folder, file))

# 사용 예시
source_folder = '/path/to/your/source/folder'
split_data(source_folder, train_ratio=0.7, validation_ratio=0.1, test_ratio=0.2, seed=42)
