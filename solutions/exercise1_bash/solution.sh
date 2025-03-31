#! /bin/bash


mkdir -p bandpass_athul # create the new directory

extensions=() #create an array for storing the extensions of each file

pushd bandpass_raw > /dev/null # save current directory and switch to "bandpass_raw"

# looping through each file in folder "bandpass_raw"
for file in *; do
	name="${file%.*}"  # extract name of the file without the extension
        ext="${file##*.}"  # extract extension
	echo "$ext" #print the extension format
	
	extensions+=("$ext") #appending the extension format to the array 'extensions'
	
	second_line=$(sed -n '2p' "$file") # captures the second line in each file
	
	# to check if the second line begins with '#' (a comment), if yes extract the word that follows (photon or energy)
	if [[ "$second_line" =~ ^#\ ?([a-zA-Z]+) ]]; then
    		keyword="${BASH_REMATCH[1]}"
	else
    		keyword="unknown" # if the second line is not beginning with '#', assign the keyword 'unknown'
	fi
	
	# defining the new name for the file with new extension '.filt'
	new_name="${name}.${keyword}.filt" #if any file does not have any info on whether it is 'photon' or 'energy' then the filename will have 'unknown' as filename.
	
	cp "$file" "../$output_dir/bandpass_athul/$new_name" # copying the files from 'bandpass_raw' folder into 'bandpass_athul' folder after renaming
done

popd > /dev/null # return to original dierectory

echo

# Print the unique extensions and their counts
echo "File extensions and their counts:"
printf "%s\n" "${extensions[@]}" | sort | uniq -c #print the number of each type of extension along with the corresponding extension





