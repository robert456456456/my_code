bob="Total running VMs: 0"
status=$("C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" list "C:\Local_VM\Windows 7 x64 sp1\Windows 7 x64 sp1.vmx")
revert_f=$("C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" revertToSnapshot  "C:\Local_VM\Windows 7 x64 sp1\Windows 7 x64 sp1.vmx" "file-save")
power_on=$("C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" start "C:\Local_VM\Windows 7 x64 sp1\Windows 7 x64 sp1.vmx")
i=0
for i in {1..450}
do
echo  -n $status > "D:\qa-automation\jenkinsPython\txt\status.txt"
FILES="D:\qa-automation\jenkinsPython\txt\status.txt"
for f in $FILES
do
value=$(<$f)
done
echo $value
echo $bob
if [ $value-eq$bob ]
then
echo snapshot_revert  
$revert_f
sleep 10
$power_on
sleep 10
echo power on vm
else
 sleep 10
 echo vn run
fi
done
exit 0