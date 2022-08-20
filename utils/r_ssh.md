后台运行:
nohup bash hello.sh &
查看输出
tail -f nohub.out
将输出保存到文件
nohup bash hello.sh >hello.log &
杀死进程
kill -TRM [$PID]


