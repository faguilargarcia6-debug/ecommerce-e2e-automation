# 🧪 Ecommerce E2E Automation Framework

Framework de automatización de pruebas End-to-End (E2E) enfocado en validar flujos críticos de plataformas ecommerce, desarrollado con **Python, Selenium y Pytest**, siguiendo el patrón **Page Object Model (POM)**.

---

## 📌 Descripción

En este proyecto desarrollé un framework de automatización orientado a pruebas **smoke** sobre funcionalidades esenciales de un ecommerce, tales como:

* Login de usuario
* Validación de acceso
* Manejo de credenciales válidas e inválidas

El diseño del framework permite su reutilización en diferentes plataformas ecommerce, desacoplando datos, lógica y localizadores.

---

## 🧱 Arquitectura del Proyecto

En el proyecto seguí una estructura modular basada en buenas prácticas de automatización:

```
project/
│
├── data/              # Page Objects (lógica de interacción)
│   └── data_checkout.py
│   └── data_login.py
│
├── locators/           # Selectores de elementos
│   └── locator_checkout.py
│   └── locator_login.py
│
├── pages/               # Datos de prueba (inputs)
│   └── cart_pages.py
│   └── checkout_pages.py
│   └── login_pages.py
│
├── tests/              # Casos de prueba
│   └── test.py
│
├── config.py           # Configuración (URL base, etc.)
├── conftest.py         # Fixtures de Pytest (driver setup)
└── README.md
```

---

## ⚙️ Tecnologías utilizadas

* **Python 3**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/ecommerce-e2e-automation.git
cd ecommerce-e2e-automation
```

---

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar pruebas

```bash
pytest -v
```

---

## 🧪 Estrategia de testing

### ✔ Pruebas positivas

* Validación de login exitoso
* Verificación de redirección a estado autenticado

### ✔ Pruebas negativas

* Credenciales inválidas
* Campos vacíos

⚠️ Nota:
Algunas pruebas negativas pueden verse afectadas por mecanismos anti-bot (CAPTCHA).
---

## 🧠 Buenas prácticas implementadas

* Separación de responsabilidades (POM)
* Uso de fixtures con Pytest
* Parametrización de datos de prueba
* Esperas explícitas (WebDriverWait)
* Diseño escalable y mantenible

---

## 📈 Próximas mejoras

* Automatización de flujo de carrito
* Automatización de checkout
* Integración con CI/CD (GitHub Actions)
* Reportes de ejecución (Allure / HTML reports)


---

## 📄 Licencia

Este proyecto es de uso educativo y demostrativo.

