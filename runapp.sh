#!/bin/bash

# Ustaw zmienne środowiskowe, jeśli jest to konieczne
# export KUBECONFIG=/ścieżka/do/twojego/kubeconfig

# Definiuj zmienne
GIT_REPO_URL="https://github.com/justdodo27/cloud-app"
APP_DIR="foods"
K8S_CONFIG_DIR="kubernetes"

# Krok 1: Pobierz najnowszą wersję aplikacji
echo "Pobieranie najnowszej wersji aplikacji..."
if [ -d "$APP_DIR" ]; then
    # Jeśli katalog już istnieje, zaktualizuj repozytorium
    cd "$APP_DIR"
    git pull
else
    # W przeciwnym razie sklonuj repozytorium
    git clone "$GIT_REPO_URL" "$APP_DIR"
    cd "$APP_DIR"
fi

# Krok 2: Uruchomienie konfiguracji Kubernetes
echo "Uruchamianie konfiguracji Kubernetes..."
cd "$K8S_CONFIG_DIR"
for file in *.yaml; do
    kubectl apply -f "$file"
done

echo "Proces wdrożenia zakończony sukcesem."
