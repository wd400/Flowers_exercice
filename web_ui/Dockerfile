FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install  --verbose

COPY . .

RUN npm run build

CMD [ "node", "dist/angular_ui/server/server.mjs" ]