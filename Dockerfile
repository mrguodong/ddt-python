FROM containers.cisco.com/doguo/rhel7_orc1.8_python:1.0.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
#RUN alias python=python3
#RUN yum-config-manager -q --enable ol7_UEKR5
#RUN yum-config-manager -q --enable ol7_latest
#RUN yum install python-devel -y
#RUN yum install python3-devel -y
RUN pip3 install -r requirements.txt
#RUN yum remove python3-devel -y
ADD . /code/
ENV ORACLE_HOME /usr/lib/oracle/18.3/client64
ENV PATH $ORACLE_HOME/bin:$PATH
ENV LD_LIBRARY_PATH $ORACLE_HOME/lib:/usr/local/lib

EXPOSE 8000
RUN chmod +x run.sh
CMD ["./run.sh"]


