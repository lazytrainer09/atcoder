# gitのadd, commitまでを行うスクリプト
# sh add_and_commit.sh target_directory
# ex) sh add_and_commit.sh 038

if [ $# -ne 1 ]; then
  echo "対象のディレクトリ名を指定してください"
  exit 0
fi

git add $1 && git commit -m "Add problem "$1
