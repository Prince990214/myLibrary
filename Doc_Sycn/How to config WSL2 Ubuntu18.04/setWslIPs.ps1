if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Change IP address of eth0 in Ubuntu"
    wsl sudo ifconfig eth0 192.168.56.25
	Write-Host "Sorry, we need to set it twice..."
	wsl sudo ifconfig eth0 192.168.56.25
}


if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process PowerShell -Verb RunAs "-NoProfile -ExecutionPolicy Bypass -Command `"cd '$pwd'; & '$PSCommandPath';`"";
    exit;
}
Write-Host "Change IP address of Windows adapter"
$var = Get-NetIPAddress -InterfaceAlias "vEthernet (WSL)"
Write-Host "Old IP: ", $var.IPAddress
Remove-NetIPAddress -InterfaceAlias "vEthernet (WSL)" -Confirm:$false
New-NetIPAddress -InterfaceAlias "vEthernet (WSL)" -AddressFamily IPv4 -IPAddress "192.168.56.1" -PrefixLength 24 >$null
$var = Get-NetIPAddress -InterfaceAlias "vEthernet (WSL)"
Write-Host "New IP: ", $var.IPAddress

#Write-Host "Press any key to continue..."
#$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")