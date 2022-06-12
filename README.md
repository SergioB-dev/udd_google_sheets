# How to use this script

1. Download the csv you wish to cross check from event brite
2. Download the json auth file from #intake-admin
3. Place that file in a directory named `gspread` in your `/.config` file in your root directory 

```
mkdir ~/.config/gspread && mv {Your_downloaded_json_file} ~/.config/gspread/service_account.json
```
Naming with the above convention will avoid the need for any customizations

4. (As long as you have python already installed on your computer) Run the script 
`python3 udd_crosscheck.py {downloaded eventbrite csv path}`

👏🏽 Viola
