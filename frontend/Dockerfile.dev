# Etap budowania
FROM node:20 as build-stage

WORKDIR /app

# Kopiowanie plików konfiguracyjnych projektu
COPY /app/package.json .
COPY /app/yarn.lock .

# Instalacja zależności projektu
RUN yarn

# Kopiowanie reszty plików projektu
COPY . .

# # Budowanie aplikacji
# RUN yarn build

CMD ["yarn", "dev", "--host"]

# # Etap uruchomienia
# FROM nginx:stable-alpine as production-stage

# # Kopiowanie zbudowanych plików do katalogu serwera Nginx
# COPY --from=build-stage /app/dist /usr/share/nginx/html

# # Nginx domyślnie nasłuchuje na porcie 80
# EXPOSE 80

# # Uruchomienie Nginx w tle
# CMD ["nginx", "-g", "daemon off;"]
