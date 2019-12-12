import sys
import os
import re


def rename_file():
    # 현재 위치 파일을 모두 가져온다.
    p = re.compile('[a-zA-Zㄱ-힣]+')
    directory = "/Users/admin/Desktop/jung/aoa/aoa/"
    for filename in os.listdir(directory):
        if filename.endswith(".htm"):
            try:
                path = os.path.join(directory, filename)
                # 파일 확장자가 (.htm)인 파일들 처리
                new_filename = re.sub(p, '', filename)
                target = os.path.join("/Users/admin/Desktop/jung/", new_filename + '.htm')
                os.rename(path, target)
            except:
                print("winerror")

def show():
    for filename in os.listdir("C:\\Users\\admin\Desktop\jung\\aoa\\"):
        print(filename)

if __name__ == "__main__":
    rename_file()

