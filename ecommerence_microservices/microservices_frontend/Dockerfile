FROM node

#WORKDIR /app/products

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

CMD ["npm","start"]