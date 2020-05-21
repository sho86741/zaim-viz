# zaim-viz

```
# cd zaim-viz/docker/python-env
# docker build ./ -t python-env
 
# cd ../elasticsearch
# mkdir -p /usr/share/elasticsearch/data
# chown 1000:0 /usr/share/elasticsearch/data
# mkdir -p /opt/elasticsearch/backup
# chown 1000:1000 /opt/elasticsearch/backup
# docker-compose up -d --build
 
# cd ../..
# vim setting.yaml
 
# docker run --rm -v `pwd`:/zaim-viz python-env python /zaim-viz/download_csv.py
 
# docker run --rm --network elasticsearch_elastic -v `pwd`:/zaim-viz python-env python /zaim-viz/insert_zaim.py /zaim-viz/$(ls -t Zaim*.csv | head -n1)
```
