#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023']

def deploy():
    env.user = 'alihhussain'
    env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
    #env.combine_stderr = False
    env.disable_known_hosts = True
    env.output_prefix = False
    env.colorize_errors = True
    env.linewise = True
    conffile=str("<VirtualHost *:80>\n  ServerName www.%s\n     ServerAlias %s\n        DocumentRoot /var/www/%s/public_html\n  ErrorLog /var/log/httpd/error.log\n     CustomLog /var/log/httpd/requests.log combined  \n</VirtualHost>" %(env.host,env.host,env.host))
    with hide('everything'):
        sudo("yum update -y")
    run("wget https://github.com/stedolan/jq/releases/download/jq-1.4/jq-linux-x86_64")
    run("chmod 755 jq-linux-x86_64")
    sudo("mv jq-linux-x86_64 /usr/bin/jq")
    sudo("yum -y install httpd")
    sudo("systemctl enable httpd.service")
    sudo("mkdir -p /var/www/%s/public_html" %env.host)
    sudo("chown -R %s:%s /var/www/%s/public_html" %(env.user,env.user,env.host))
    sudo("chmod -R 755 /var/www")
    run("curl -O https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/Automation%20Demo/TestWebPage/testweb.zip")
    run("unzip /home/alihhussain/testweb.zip -d /var/www/%s/public_html/" %env.host)
    run("mv /var/www/%s/public_html/index.htm /var/www/%s/public_html/index.html" %(env.host,env.host))
    run("""curl -H Metadata:true "http://169.254.169.254/metadata/instance?api-version=2017-03-01" | jq .network.interface[0].ipv4.ipaddress[0].ipaddress | tr -d '"' > /tmp/instance.ip""")
    run("""sed -i "s#server_name#$(sudo cat /tmp/instance.ip)#g" /var/www/%s/public_html/index.html""" %env.host)
    sudo("mkdir /etc/httpd/sites-available")
    sudo("mkdir /etc/httpd/sites-enabled")
    sudo("echo 'IncludeOptional sites-enabled/*.conf' >> /etc/httpd/conf/httpd.conf")
    sudo("echo '%s' > /etc/httpd/sites-available/%s.conf" %(conffile,env.host))
    sudo("ln -s /etc/httpd/sites-available/%s.conf /etc/httpd/sites-enabled/%s.conf" %(env.host,env.host))
    sudo("service httpd stop")
    sudo("service httpd start")
