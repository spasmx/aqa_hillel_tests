FROM python:3.10

COPY . /app

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install wget curl gnupg2 unzip default-jre


RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb && \
    apt-get -y install ./chrome.deb && \
    rm ./chrome.deb

RUN wget https://chromedriver.storage.googleapis.com/$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chown root:root /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

RUN pip install --upgrade pip && \
    pip install pytest pytest-xdist allure-pytest selenium requests



WORKDIR /app

CMD [ "pytest", "-n=4", "--alluredir", "./allure-results" ]