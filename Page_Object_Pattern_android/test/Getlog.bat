echo off

echo File name should be sending in 2nd parameter in command prompt

setlocal enableDelayedExpansion


set Folder=%1


mkdir %Folder%

adb shell  cat /sys/kernel/debug/boardid/boardid > %Folder%\boardid.txt
adb shell  cat /sys/kernel/debug/boardid/common/common > %Folder%\boardid_common.txt
adb shell  dmesg > %Folder%\dmesg.txt
adb shell ps > %Folder%\ps.txt

adb shell  logcat -v time -d -b radio > %Folder%\logcat_ril.txt
adb shell  logcat -v time -d -b radio -s AT > %Folder%\logcat_at.txt
adb shell  logcat -v time -d > %Folder%\logcat.txt

adb pull   /data/logs   %Folder%/logs_all.txt

mkdir %Folder%\android_logs
adb pull   /data/log/android_logs  %Folder%/android_logs

mkdir %Folder%\dumplog
adb pull   /data/dumplog %Folder%\dumplog

mkdir %Folder%\dontpanic
adb pull   /data/dontpanic %Folder%\dontpanic\

mkdir %Folder%\dropbox
adb pull   /data/system/dropbox         %Folder%\dropbox

mkdir %Folder%\tombstones
adb pull   /data/tombstones             %Folder%\tombstones

mkdir %Folder%\anr
adb pull   /data/anr                    %Folder%\anr 

mkdir %Folder%\dumpsys_meminfo
adb shell dumpsys meminfo > %Folder%\dumpsys_meminfo\info.txt


adb shell dumpsys jobscheduler > %Folder%/jobscheduler.txt
adb shell  bugreport > %Folder%/bug_report.txt


::adb shell "cat /etc/bluetooth/bt_stack.conf | grep FileName"
mkdir %Folder%\bt
adb pull   /data/log/bt                   %Folder%\bt



adb shell "rm /data/dontpanic/*"
adb shell "rm /data/system/dropbox/*"
adb shell "rm /data/corefile/*"
adb shell "rm /data/tombstones/*"
adb shell "rm /data/anr/*"
adb shell "rm /data/android_logs/*"
adb shell "rm -rR /data/log/android_logs/*.*"
adb shell "rm -rR /data/log/bt/*.*"


echo log collection complete
pause