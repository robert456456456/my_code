status=$("C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" list "C:\Local_VM\Windows 7 x64 sp1\Windows 7 x64 sp1.vmx")
echo  -n $status > "D:\qa-automation\jenkinsPython\run_local_vm\status.txt"
FILES="D:\qa-automation\jenkinsPython\run_local_vm\status.txt"
for f in $FILES
do
value=$(<$f)
done
echo $value