file="env.variables"

while read -r line; do
    export $line;
done <$file 