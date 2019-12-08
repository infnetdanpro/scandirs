# scandirs
Simple program for scan dirs and report result in CSV into the current folder. 
This program answer for these questions:
 - how to find big files?
 
 It's very small console util.
 
## Example usage
0. Download [the latest release](https://github.com/infnetdanpro/scandirs/releases)
1. Run cmd.exe
2. Move to directory with file scandir.exe
3. Run program: 
> \> scandir.exe -d D:\

or

> \> scandir.exe -d C:/Users/Max/Downloads

4. The report will be created in the same folder as "Report_scandir_<timestamp>.csv"


### Alternative use
Create the .bat file with entire: 
> scandir.exe -d D:\ 

Save into file and run "yourfile.bat" 


code written in 2017, remastered in 2019.
