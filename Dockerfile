FROM node:12-alpine as builder
WORKDIR /app
ADD ./package.json ./package-lock.json ./
RUN npm ci
ADD ./ ./
RUN npm run build 

FROM nginx:stable-alpine as app
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]