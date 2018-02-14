wav_file=$1
output_file=a.out
python3 get_freq.py $wav_file 2> /dev/null > $output_file
