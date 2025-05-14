#want to remove backup files from path /www/html/access.log which are older than 7 days
path="/www/html/access.log"
#find command to find files older than 7 days and delete them
find $path -type f -name "*.log" -mtime +7 -exec rm {} \ ;