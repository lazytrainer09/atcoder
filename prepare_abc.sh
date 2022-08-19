#!/bin/bash
# abcの準備用スクリプト
# sh prepare_abc.sh コンテスト番号
# ex) sh prepare_abc.sh 205

contest_no=$1
problems=("a" "b" "c" "d" "e")

files=(
    "answer.py"
    "input.txt"
)

for problem in "${problems[@]}"; do
    path="${contest_no}/${problem}"
    mkdir -p $path

    # 事前に作成したいファイルを以下に記載
    for file in "${files[@]}"; do
        touch $path/$file
    done
done
