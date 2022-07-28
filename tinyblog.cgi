#!/bin/sh

read posted
FILE="../logs.txt" #テキストファイルを参照
log=`echo $posted | sed 's/comment=//' | tr % \= | nkf -WmQ` #postedをsedに渡し、trに渡し、nkfに渡す
if [ $log != "" ] ; then #if文で空欄の時以外で実行
echo "<dt>"名無しの大学生 "`date "+%F %T"`</dt><dd>$log</dd>" >> $FILE #dateを<dt>タグ、logを<dd>タグに入れる
fi
echo "Content-Tyepe: text/html"
echo ""
echo "<!doctype html>"
echo "<html lang=\"ja\">"
echo "<head>"
echo "<meta charset=\"utf-8\" />"
echo "<title>tinyblog</title>"
echo "</head>"
echo "<body>"
echo "<h1>Tiny blog</h1>"
echo "<h2>Log</h2>"
echo "<dl>"
cat $FILE #catコマンドで内容を表示させる
echo "</dl>"
echo "<p>レスを投稿する↓</p>"
echo "<form action=\"tinyblog.cgi\" method=\"POST\">"
echo "<input type=\"test\" name=\"comment\" value=\"\"/>"
echo "<input type=\"submit\"/>"
echo "</form>"
echo "</body>"
echo "</html>"
