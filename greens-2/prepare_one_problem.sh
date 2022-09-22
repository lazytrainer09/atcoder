#!/bin/bash
# 任意の問題の準備用スクリプト

# コンテスト-コンテスト番号-問題番号で入力
# ex) ABC-234-E

mkdir $1
code $1/input.txt

file_path=/Users/futami/workspace/atcoder/template.py

cp $file_path $1/answer.py
code $1/answer.py
