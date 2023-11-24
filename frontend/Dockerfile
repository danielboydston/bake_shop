FROM node:21

# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#      && apt-get -y install --no-install-recommends yarn

RUN npm i -g pnpm

WORKDIR /usr/src/app

COPY app/package*.json ./

RUN pnpm install
# If you are building your code for production
# RUN npm ci --omit=dev

# Bundle app source
COPY app/ .

EXPOSE 5173
CMD [ "pnpm", "start" ]