#!/bin/bash

# Define la estructura de directorios y archivos
declare -A structure=(
    ["01_utilities/_mixins.scss"]=""
    ["01_utilities/_variables-css.scss"]=""
    ["01_utilities/_variables-sass.scss"]=""
    ["01_utilities/_keyframes.scss"]=""
    ["02_base/_font-family.scss"]=""
    ["02_base/_reset.scss"]=""
    ["03_layout/_l-columns.scss"]=""
    ["03_layout/_l-flex.scss"]=""
    ["03_layout/_l-grid.scss"]=""
    ["03_layout/_l-piramide.scss"]=""
    ["04_components/_c-accordion.scss"]=""
    ["04_components/_c-alert.scss"]=""
    ["04_components/_c-button.scss"]=""
    ["04_components/_c-card.scss"]=""
    ["04_components/_c-desplegable.scss"]=""
    ["04_components/_c-formulario.scss"]=""
    ["04_components/_c-image.scss"]=""
    ["04_components/_c-panel.scss"]=""
    ["04_components/_c-placeholder.scss"]=""
    ["04_components/_c-process.scss"]=""
    ["04_components/_c-tabla.scss"]=""
    ["05_pages/.gitkeep"]=""
    ["06_global/_g-background.scss"]=""
    ["06_global/_g-border.scss"]=""
    ["06_global/_g-color.scss"]=""
    ["06_global/_g-font-size.scss"]=""
    ["06_global/_g-height.scss"]=""
    ["06_global/_g-margin.scss"]=""
    ["06_global/_g-padding.scss"]=""
    ["06_global/_g-position.scss"]=""
    ["06_global/_g-shadow.scss"]=""
    ["06_global/_g-text-align.scss"]=""
    ["06_global/_g-text-decoration.scss"]=""
    ["06_global/_g-width.scss"]=""
    ["main.scss"]=""
)

# Crear los directorios y archivos
for path in "${!structure[@]}"; do
    dir=$(dirname "$path")
    mkdir -p "$dir"   # Crear el directorio si no existe
    touch "$path"     # Crear el archivo
done

echo "Estructura de directorios y archivos creada con éxito."
