#!/bin/sh
n=100
for i in $(seq 1 $n); do
  unified_dir=$(dirname BLAST-results/unified_${i}.txt)
  mkdir -p "$unified_dir"
  cat BLAST*/num${i}*txt > BLAST-results/unified_${i}.txt
done

search_pattern='Query= '
clean_content() {
  sed 's/<[^>]*>//g' | tr -d '\r' | awk '!/^>/ {print $0} /^>/ {print $0}'
}

find . -type f | while read -r file; do
  temp_file=$(mktemp)
  clean_content < "$file" > "$temp_file"
  match=$(grep -m 1 "$search_pattern" "$temp_file")
  if [ "$match" ]; then
    new_name=$(echo "$match" | sed -n 's/.*Query= \(TraesCS[^ ]*\).*/\1/p')
    new_name=$(echo "$new_name" | tr -d '\r')
    if [ "$new_name" ]; then
      mv "$file" "$(dirname "$file")/$new_name"
      echo "Renamed $file to $(dirname "$file")/$new_name"
    else
      echo "No valid new name found in $file"
    fi
  fi
  rm "$temp_file"
done
