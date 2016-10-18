echo 'Deleting old directory...'
echo '#########################'
curl -XDELETE http://127.0.0.1:9200/music
echo 'Creating new directory...'
echo '#########################'
curl -XPOST http://127.0.0.1:9200/music -d @setup.json
echo 'Attempting to remove old json file...'
echo '#########################'
rm music.json
echo 'Writing to new json file...'
echo '#########################'
python utils2.py
echo 'Pushing new json to ES...'
echo '#########################'
curl -s -XPOST http://127.0.0.1:9200/_bulk --data-binary @music.json
