---
layout: default
title: Configuración Inicial
description: Guía para configurar el proyecto Tintum.app desde cero
category: guide
---

# Configuración Inicial

Esta guía te ayudará a configurar el proyecto Tintum.app desde cero.

## Requisitos Previos

- Node.js (v16 o superior)
- Firebase CLI instalado globalmente
- Cuenta Firebase: `denis@tintum.app`
- Git configurado

## Paso 1: Instalar Firebase CLI

```bash
npm install -g firebase-tools
```

## Paso 2: Autenticarse en Firebase

```bash
firebase login
```

Asegúrate de usar la cuenta: `denis@tintum.app`

## Paso 3: Inicializar Firebase en el Proyecto

```bash
cd tintum-app
firebase init
```

Durante la inicialización, selecciona:
- ✅ Hosting
- ✅ Firestore

## Paso 4: Configurar el Proyecto

El archivo `firebase.json` ya está configurado con:
- Hosting apuntando a la carpeta `web/`
- Reglas de Firestore
- Índices de Firestore

## Paso 5: Verificar la Configuración

```bash
firebase projects:list
```

Deberías ver tu proyecto de Firebase listado.

## Siguiente Paso

Una vez configurado, puedes proceder con el [despliegue inicial]({{ '/despliegue' | relative_url }}).

