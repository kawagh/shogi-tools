for i in `seq -f '%03g' 1 85`; do
    echo "from_sfen${i}.svg"
    convert "from_sfen${i}.svg" "from_sfen${i}.png"
done
