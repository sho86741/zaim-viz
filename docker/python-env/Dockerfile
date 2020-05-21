FROM python

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable unzip && \
    mkdir -p /opt/chrome && \
    curl -sS -o /opt/chrome/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
    cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip && rm -f chromedriver_linux64.zip && \
    pip install --upgrade pip && \
    pip install selenium django elasticsearch pyyaml && \
    wget -q https://ipafont.ipa.go.jp/IPAexfont/ipaexg00401.zip && \
    unzip ipaexg00401.zip -d /usr/share/fonts && rm -f ipaexg00401.zip && \
    fc-cache -fv

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome
