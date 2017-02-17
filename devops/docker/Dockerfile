FROM daocloud.io/ubuntu
MAINTAINER zhengwen "zhengwen@51lsh.com"
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.163.com\/ubuntu\//g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python2.7 python-dev python-distribute python-pip ipython
RUN apt-get install -y iputils-ping
RUN apt-get install -y net-tools

ADD pip.conf ~/.pip/
RUN pip install wheel
RUN pip install requests 
RUN apt-get install -y libffi-dev libxml2-dev libxslt-dev lib32z1-dev libssl-dev
RUN pip install lxml scrapy scrapyd
RUN pip install redis
RUN pip install pymongo
RUN pip install scrapy-redis

RUN mkdir /usr/local/spider
RUN apt-get install -y supervisor
RUN echo_supervisord_conf > /etc/supervisor/conf.d/supervisord.conf
RUN sed -i '$a [supervisord]\nnodaemon=true\n[program:scrapyd]\ncommand=scrapyd\ndirectory=/usr/local/spider' /etc/supervisor/conf.d/supervisord.conf
ENV SPIDER_ENV product

RUN mkdir /etc/scrapyd
ADD scrapyd.conf /etc/scrapyd/scrapyd.conf

EXPOSE 6800
CMD ["/usr/bin/supervisord"]	
