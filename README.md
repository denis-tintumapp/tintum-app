# Tintum.app - Proyecto Web

Proyecto web de Tintum.app hosteado en Firebase.

## 📚 Documentación

La documentación completa está disponible en la carpeta [`docs/`](docs/). Está escrita en Markdown y utiliza plantillas Liquid para una mejor organización.

Para ver la documentación localmente con Jekyll:

```bash
cd docs
bundle install
bundle exec jekyll serve
```

## 🔗 Enlaces

- **Repositorio**: [GitHub](https://github.com/denis-tintumapp/tintum-app)
- **Documentación**: Ver carpeta `docs/`
- **Firebase Console**: https://console.firebase.google.com/project/tintum-web/overview
- **Hosting URL**: https://tintum-web.web.app
- **Dominio Personalizado**: https://tintum.app (ver [guía de configuración](docs/configurar-dominio-personalizado.md))

## Configuración

### Cuenta Firebase
- **Email**: denis@tintum.app
- **Hosting**: Firebase Hosting
- **Base de datos**: Firestore

## Estructura del Proyecto

```
tintum-app/
├── web/              # Archivos estáticos para hosting
│   ├── js/           # JavaScript
│   ├── css/          # Estilos
│   ├── images/       # Imágenes
│   ├── icons/        # Iconos PWA
│   └── index.html    # Página principal
├── firebase.json      # Configuración de Firebase
├── firestore.rules    # Reglas de seguridad de Firestore
└── firestore.indexes.json  # Índices de Firestore
```

## Comandos Útiles

### Inicializar Firebase (si aún no está inicializado)
```bash
firebase login
firebase init
```

### Desplegar a Firebase Hosting
```bash
firebase deploy --only hosting
```

### Desplegar reglas de Firestore
```bash
firebase deploy --only firestore:rules
```

### Desplegar índices de Firestore
```bash
firebase deploy --only firestore:indexes
```

### Desplegar todo
```bash
firebase deploy
```

## Desarrollo Local

Para probar localmente con Firebase Emulator:
```bash
firebase emulators:start
```

## Configurar Dominio Personalizado

Para configurar `tintum.app` como dominio personalizado, consulta la [guía completa](docs/configurar-dominio-personalizado.md).

Verificar configuración DNS:
```bash
./configurar-dominio.sh
```

## Notas

- Asegúrate de estar autenticado con la cuenta correcta: `denis@tintum.app`
- Verifica la configuración del proyecto en Firebase Console
- El dominio personalizado `tintum.app` requiere registros A y AAAA (no CNAME) en Namecheap

