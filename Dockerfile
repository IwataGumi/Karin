FROM python:3.8.10
USER root

RUN apt update
RUN apt install locales -y && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt install -y vim less

# Install Node
ENV NODE_VERSION=18.16.1
RUN apt install -y curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
RUN node --version
RUN npm --version

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /root/Gachiniii

WORKDIR /root/Gachiniii
# Install Dependencies

# Install nodemon
RUN npm install -g nodemon

# ffmpeg
RUN apt install -y ffmpeg

# Install poetry
COPY poetry.lock /root/Gachiniii/
COPY pyproject.toml /root/Gachiniii/

RUN pip install poetry
ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false
RUN poetry install --with dev

# Update pip and setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
