# myawesomescript.sh
# jpflug 2019.01.16

# read in script output
fn="$1"
# define the output file and initialize
out_fn=${fn%.*}_lettercount.txt
touch $out_fn

# for every letter in the alphabet
for alph in {a..z}
do 

# output for letter being used
out1=$alph
# output for number of letters
out2=`grep -i ^$alph $fn | wc -w`
# display and write outputs with each other
echo "$out1 $out2" >> $out_fn

done
