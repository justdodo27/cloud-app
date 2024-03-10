# Etap budowania
FROM node:20 as build-stage
ARG VUE_APP_BACKEND_URL

WORKDIR /

# Kopiowanie plików konfiguracyjnych projektu
# COPY /app/package.json ./package.json
# COPY /app/yarn.lock ./yarn.lock
# COPY /app/vite.config.js ./vite.config.js
# COPY /app/tailwind.config.js ./tailwind.config.js
# COPY /app/postcss.config.js ./postcss.config.js

# Kopiowanie reszty plików projektu
COPY . .
WORKDIR /app
# Instalacja zależności projektu
RUN yarn
RUN yarn add @vitejs/plugin-vue --dev
RUN yarn add tailwindcss autoprefixer postcss

# Budowanie aplikacji
RUN echo "VITE_BACKEND_URL=${VUE_APP_BACKEND_URL}" > .env
RUN yarn build

# Etap uruchomienia
FROM nginx:stable-alpine as production-stage

# Kopiowanie zbudowanych plików do katalogu serwera Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
# Nginx domyślnie nasłuchuje na porcie 80
EXPOSE 80

# Uruchomienie Nginx w tle
CMD ["nginx", "-g", "daemon off;"]
