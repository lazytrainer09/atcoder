#!/bin/bash
# 任意の問題の準備用スクリプト

# コンテスト-コンテスト番号-問題番号で入力
# ex) ABC-234-E
problem_name=$1

# 事前に作成したいファイルを以下に記載
files=(
    "answer.py"
    "input.txt"
)

mkdir $1

for file in "${files[@]}"; do
    code $1/$file
done
