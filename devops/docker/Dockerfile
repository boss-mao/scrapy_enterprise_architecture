FROM daocloud.io/ubuntu
MAINTAINER mao "mail.zhengwen@gmail.com"
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.163.com\/ubuntu\//g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python2.7 python-dev python-distribute python-pip ipython
RUN apt-get install -y iputils-ping
RUN apt-get install -y net-tools

ADD pip.conf ~/.pip/
RUN pip install requests 
RUN apt-get install -y libffi-dev libxml2-dev libxslt-dev lib32z1-dev libssl-dev
RUN pip install lxml scrapy scrapyd
RUN pip install redis
RUN pip install pymongo
RUN pip install scrapy-redis

RUN mkdir /home/code
RUN apt-get install -y supervisor
RUN echo_supervisord_conf > /etc/supervisor/conf.d/supervisord.conf
RUN sed -i '$a [supervisord]\nnodaemon=true\n[program:scrapyd]\ncommand=scrapyd\ndirectory=/home/code' /etc/supervisor/conf.d/supervisord.conf
EXPOSE 6800 
CMD ["/usr/bin/supervisord"]	
