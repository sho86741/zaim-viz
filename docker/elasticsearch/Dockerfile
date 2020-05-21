FROM docker.elastic.co/elasticsearch/elasticsearch:7.7.0

RUN echo 'path.repo: ["/opt/elasticsearch/backup"]' >> /usr/share/elasticsearch/config/elasticsearch.yml

RUN mkdir -p /opt/elasticsearch/backup && chown -R elasticsearch:elasticsearch /opt/elasticsearch/backup
