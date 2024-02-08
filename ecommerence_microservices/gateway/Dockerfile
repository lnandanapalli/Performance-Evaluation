FROM node

#WORKDIR /app/products

COPY package.json .

RUN npm install

COPY . .

EXPOSE 8000

CMD ["node","index.js"]