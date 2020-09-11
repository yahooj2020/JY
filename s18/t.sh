for url in `cat t.txt`
do
    wget "$url"
    sleep 0.5
done 
