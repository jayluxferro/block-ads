#!/bin/bash

rm -rf combined_list.txt

for link in $(cat links.txt); do
  echo "[-] Processing $link"
  # Extract the filename from the link
  filename=$(basename "$link")

  # Download the file
  wget -q "$link" -O "$filename"

  # Check if the file was downloaded successfully
  if [ $? -eq 0 ]; then
    echo -e "[+] Downloaded $filename successfully.\n"

    # Append the content to combined_list.txt
    cat "$filename" >>combined_list.txt

    # Remove the downloaded file
    rm "$filename"
  else
    echo "[-] Failed to download $link"
  fi
done

# Add custom_list.txt to combined_list.txt
cat ../list.txt >>combined_list.txt

python3 ./format_list.py
