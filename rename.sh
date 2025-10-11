#!/bin/bash

# Directory containing the files
DIR="$1"

# Counter for numbering
n=1

# Loop through each file in the directory
for file in "$DIR"/*; do
  # Skip if not a file
  [ -f "$file" ] || continue

  # Extract file extension
  ext="${file##*.}"

  # Construct new file name with prefix "bild-" and number
  newname="$DIR/bild-$n.$ext"

  # Rename the file
  mv -i "$file" "$newname"

  # Increment the counter
  ((n++))
done

