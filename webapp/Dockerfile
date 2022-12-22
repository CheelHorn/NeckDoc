FROM node:lts-alpine
WORKDIR /app
COPY package.json /app/package.json
RUN npm install
COPY . .
EXPOSE 8080
ENTRYPOINT [ "npm", "run", "serve"]