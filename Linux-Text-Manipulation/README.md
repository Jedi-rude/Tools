# Gathering FQDN servers
Linux BASH text manipulation in order to extract all the server names from the common website main page.
Gathering as many FQDN server names as possible with minimum traffic generation. While browsing the websites, you notice that their main page contains links to many of their services which are located on different servers.

## Scripts Usage
Use followings orders to get domain names and ip addresses.
- [wget](https://www.gnu.org/software/wget/)
- [index.sh](https://github.com/AungZayMyo/Tools/blob/main/Linux-Text-Manipulation/index.sh)
- [domain.sh](https://github.com/AungZayMyo/Tools/blob/main/Linux-Text-Manipulation/domain.sh)
- [ip.sh](https://github.com/AungZayMyo/Tools/blob/main/Linux-Text-Manipulation/ip.sh)

Downloads Scripts and Give Permissions
```
chmod +x index.sh domain.sh ip.sh
```

### wget

First, run wget utility to download index page. use following commands ``` wget [domain] ```.
<p align="center"><img src="https://github.com/AungZayMyo/Tools/assets/154745254/5f8e16e7-d73f-45a3-98d5-73a822f59712" width="500px" height="250px"><br>Figure (1)</p>

### index.sh
run index script to find domains from index file. run following scripts ```./index.sh index.html [domainname]```. and type ``` ls ``` and see contents from ``` cisco-domain.txt ```. We gots domain names.
<p align="center"><img src="https://github.com/AungZayMyo/Tools/assets/154745254/235ee15d-e60e-416f-b908-b617f4bcf2de" width="500px" height="250px"><br>Figure (2)</p>


### domain.sh
next run domain script to identify alive hosts. run following scripts ``` ./domain.sh cisco-domain.txt > cisco-hosts.txt ```. and type ``` ls ``` and see contents from ``` cisco-hosts.txt ```. We gots alive hosts.
<p align="center"><img src="https://github.com/AungZayMyo/Tools/assets/154745254/636725cb-91c9-4982-b81b-a1cfe11b85ae" width="500px" height="250px"><br>Figure (3)</p>


### ip.sh
finally, run ip script to filter ip from hosts. run following scripts ``` ./ip.sh cisco-hosts.txt > cisco-ip.txt ```. and type ``` ls ``` and see contents from ``` cisco-ip.txt ```. We gots alive ip addresses.
<p align="center"><img src="https://github.com/AungZayMyo/Tools/assets/154745254/e41d64cb-6c12-4e4f-a1ca-3c94bdf7d6a5" width="500px" height="250px"><br>Figure (4)</p>


## Conclusion 

Do more Practice and Expert it!. <br>
**3/23/2024** <br>
Contributed By - Jord@n
