# 🗃️ Base_de_datos
Este repositorio contiene el desarrollo de un proyecto para la clase de Bases de Datos, en el cual se implementa una interfaz gráfica en Python para la gestión de una base de datos relacional. El objetivo principal es aplicar los conceptos aprendidos en clase, incluyendo el diseño de bases de datos, consultas SQL y la conexión entre una base de datos y una aplicación.

La interfaz permite realizar operaciones CRUD (crear, leer, actualizar y eliminar) sobre los datos de forma amigable para el usuario.

🔧 Tecnologías utilizadas

 - Python como lenguaje de programación
 - Tkinter para la interfaz gráfica
 - MySQL como sistema de gestión de base de datos
 - mysql-connector-python para la conexión entre Python y MySQL

🎯 Objetivos del proyecto

  - ✅ Diseñar y modelar una base de datos funcional.
  - ✅ Desarrollar una interfaz gráfica con Python.
  - ✅ Conectar la interfaz a la base de datos.
  - ✅ Permitir al usuario interactuar fácilmente con los datos mediante operaciones CRUD.

▶️ Funcionamiento

  - Al iniciar el programa, se presenta una ventana con botones que permiten ejecutar las principales funciones del sistema.
  - Cada botón está asociado a una función específica: listar oficinas, crear oficinas, listar clientes y buscar clientes por ciudad.
  - Las consultas SQL son ejecutadas de forma segura mediante parámetros, evitando inyecciones.
  - Las funciones que requieren entrada del usuario utilizan cuadros de diálogo (simpledialog.askstring) para mejorar la experiencia.
  - La salida de las operaciones se muestra en un área de texto con scroll, la cual se limpia automáticamente antes de cada nueva operación para evitar confusión.

💡 Posibles mejoras

  - 🔒 Uso de variables de entorno o archivos .env para manejar las credenciales de la base de datos de forma segura.
  - 🎨 Agregar validación de datos en los formularios antes de insertar o modificar registros.
  - 🔄 Implementar funciones de actualización y eliminación de registros (actualmente solo se listan y crean).
  - 🔍 Mejorar la búsqueda de clientes con filtros avanzados (por país, nombre parcial, etc.).
  - 📊 Agregar estadísticas o reportes visuales a partir de los datos (por ejemplo, número de clientes por ciudad).


🏁 Cómo ejecutar el proyecto

  - Clona este repositorio:
    
        git clone https://github.com/sergioAGC27/Base_de_datos.git
    
  - Instala los requisitos:

        pip install mysql-connector-python
    
  - Asegúrate de tener MySQL instalado y la base de datos llamada jardineria:

        https://gist.github.com/josejuansanchez/c408725e848afd64dd9a20ab37fba8c9
    
  - ⚠️ IMPORTANTE: En el archivo db.py, debes ingresar tus credenciales de acceso a la base de datos
    
  - Ejecuta la aplicación:
    
         python main.py
    
