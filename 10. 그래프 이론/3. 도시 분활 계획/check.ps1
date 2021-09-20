$check_file = "solution_out.txt"

if (Test-Path $check_file){
    Remove-Item $check_file
}

Get-Content data.txt | python solution_v7.py | Add-Content solution_out.txt

if (Test-Path $check_file){
    #fc.exe out.txt $check_file
    Compare-Object (Get-Content out.txt) (Get-Content $check_file)
} else {
    # Write-Error "py에서 오류 발생"
}

