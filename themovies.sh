#! /usr/bin/env bash
export IFS=$'\n'
curl https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss |grep --color '<description>.*</description>' |  sed 's/<description><!\[CDATA\[//' |sed 's/\]\]><\/description>//'>synopses.txt
array=($(cat synopses.txt))
t=$(curl https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss| grep --color '<title>.*</title>' |  sed 's/<title><!\[CDATA\[//' |sed 's/\]\]><\/title>//')
while true
do
echo "$t"
echo "Choose a movie (1 -10) > "
read movie
echo "${array[$movie]}"
echo "Press enter to return"
read enter

done