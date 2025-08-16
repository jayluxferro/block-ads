#!/bin/bash

rm -rf combined_list.txt

for link in $(cat links.txt); do
  echo "Processing $link"
  # Extract the filename from the link
  filename=$(basename "$link")

  # Download the file
  wget -q "$link" -O "$filename"

  # Check if the file was downloaded successfully
  if [ $? -eq 0 ]; then
    echo "Downloaded $filename successfully."

    # Append the content to combined_list.txt
    cat "$filename" >>combined_list.txt

    # Remove the downloaded file
    rm "$filename"
  else
    echo "Failed to download $link"
  fi
done
