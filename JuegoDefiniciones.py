import random

# Códigos de color ANSI
class Colores:
    VERDE = '\033[92m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BLANCO = '\033[97m'
    NEGRITA = '\033[1m'
    RESET = '\033[0m'

# Diccionario con todos los conceptos y sus definiciones
conceptos = {
    "B2B": "Transacción o relación comercial de empresa a empresa.",
    "B2C": "Transacción o relación comercial entre una empresa y un cliente final.",
    "Back-Office": "Relación de actividades y procesos de carácter administrativo que tienen que ver con los procesos internos de una empresa.",
    "BI": "Inteligencia de negocio. Conjunto de estrategias y herramientas para la extracción, análisis y visualización de información empresarial.",
    "Big Data": "Procesamiento de volúmenes muy grandes de datos de todo tipo.",
    "BOM": "Lista de materiales. Aplicación básica para la gestión de listas de materiales e inventario necesarios para la fabricación de productos.",
    "BP": "Proceso de negocio. Conjunto de tareas relacionadas y ordenadas que proporcionan un producto o servicio.",
    "BPM": "Gestión de los procesos de negocio orientado a la gestión y mejora continua de los procesos empresariales.",
    "BSC": "Cuadro de mando integral. Metodología de gestión estratégica que posibilita un seguimiento detallado del plan estratégico empresarial.",
    "Cloud Computing": "Computación en la nube. Servicios de computación hardware y software proporcionados a través de Internet.",
    "CMS": "Sistema gestor de contenidos orientado a la publicación y gestión de contenidos accesibles mediante servicio web.",
    "Compliance": "Procedimientos que garantizan la observancia y cumplimiento de la normativa interna y legislación actual.",
    "CRM": "Sistema de gestión de las relaciones con los clientes que asiste en la consecución y mantenimiento de la cartera de clientes.",
    "Dataset": "Conjunto estructurado de datos que sirve para análisis, informes o toma de decisiones en la empresa.",
    "Data Mining": "Minería de datos. Conjunto de técnicas orientadas a buscar patrones no evidentes y tendencias en grandes bases de datos.",
    "Data Warehouse": "Almacén de datos que contiene también los metadatos sobre la procedencia, frecuencia de actualización y fiabilidad de los datos.",
    "DMS": "Sistema de gestión documental orientado a la gestión y mantenimiento de documentación interna de la empresa.",
    "DSS": "Sistema de ayuda a la toma de decisiones que produce información de valor para asistir a la dirección de la empresa.",
    "E-commerce": "Comercio electrónico. Comercialización de productos y servicios a través de Internet.",
    "EDI": "Intercambio electrónico de datos. Sistemas y estándares para la transmisión y procesamiento de datos entre sistemas empresariales.",
    "Eficacia": "En el entorno empresarial, consiste en alcanzar las metas establecidas en la empresa.",
    "Eficiencia": "En el entorno empresarial, se refiere a lograr las metas con la menor cantidad de recursos posible.",
    "ERP": "Sistema de planificación de recursos empresariales integrado que permite automatizar procesos y compartir información entre departamentos.",
    "ERP Vertical": "ERP adaptado a las necesidades específicas de un sector o industria, optimizando sus procesos particulares.",
    "ERP Horizontal": "ERP con funcionalidades generales aplicables a múltiples sectores, que cubre procesos empresariales comunes.",
    "ETL": "Conjunto de herramientas y procesos para la extracción, transformación y carga de datos entre diferentes sistemas.",
    "Front-Office": "Relación de actividades y procesos empresariales realizados de cara al cliente.",
    "Gestión empresarial": "Conjunto de acciones y estrategias que persigue el objetivo de mejorar el funcionamiento general de una empresa.",
    "Granularidad": "Nivel de detalle de los datos o información; mayor granularidad permite análisis más precisos.",
    "IaaS": "Infraestructura como servicio. Modalidad de cloud donde el cliente paga por recursos computacionales como CPU y almacenamiento.",
    "Insumo": "Recurso, bien o servicio utilizado en un proceso productivo o de negocio para generar productos o resultados.",
    "Insight": "Conocimiento útil y valioso extraído del análisis de datos que permite tomar decisiones estratégicas.",
    "IoT": "Internet de las cosas. Interconexión de dispositivos electrónicos a través de Internet.",
    "KMS": "Sistema de gestión del conocimiento orientado a la gestión de documentación, manuales y procedimientos organizacionales.",
    "Know-how": "Conocimientos no protegidos de una organización que le confieren una ventaja competitiva frente a competidores.",
    "KPI": "Indicador clave de rendimiento. Indicadores que permiten medir magnitudes o áreas de interés.",
    "MIS": "Sistema de información empresarial orientado a resolver problemas empresariales mediante soluciones TIC.",
    "MRP": "Planificación de los requerimientos de material. Sistema orientado a la gestión de los requisitos de materiales.",
    "MRP II": "Planificación de los recursos de fabricación. Sistema orientado a la gestión global de la fabricación y producción.",
    "OLAP": "Bases de datos multidimensionales orientadas al procesamiento analítico de datos empresariales.",
    "On-Premise": "Instalación de un sistema en local, cuando los servicios se ubican en la propia empresa.",
    "PaaS": "Plataforma como servicio. Modalidad de cloud donde el cliente alquila una plataforma de desarrollo y despliegue.",
    "PLM": "Gestión del ciclo de vida de productos en sus diferentes fases de inicio a fin.",
    "POS": "Terminal de punto de venta orientado a la gestión de los procesos de venta de un establecimiento.",
    "Productividad": "Relación entre los productos obtenidos y los insumos utilizados en un período determinado.",
    "ROI": "Retorno de la inversión. Cálculo del tiempo que se necesita para recuperar lo invertido con los beneficios generados.",
    "SaaS": "Software como servicio. Modalidad de cloud donde el proveedor ofrece licencias de uso de un software a través de Internet.",
    "SCM": "Gestión de la cadena de suministro orientada a la gestión del suministro de insumos y materiales.",
    "Sistema de información": "Infraestructura informática y recursos tecnológicos que sostienen los procesos automatizados de una empresa.",
    "Sostenibilidad": "Búsqueda del equilibrio entre el crecimiento económico y el cuidado del entorno a largo plazo.",
    "SRM": "Gestión de las relaciones con los proveedores de productos o servicios de la empresa.",
    "TIC": "Tecnologías de información y comunicación. Herramientas hardware y software para almacenamiento y procesamiento de información.",
    "Transacción": "Proceso tecnológico que genera, modifica o intercambia datos en un sistema de información.",
    "Trazabilidad": "Capacidad de seguir y documentar el historial y aplicación de un producto, proceso o dato a lo largo de su ciclo de vida.",
    "Workflow": "Flujo de trabajo. Automatización de los procesos de la empresa para que la información y tareas circulen correctamente."
}

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida y las instrucciones"""
    print(f"{Colores.CYAN}{Colores.NEGRITA}{'=' * 60}")
    print("JUEGO DE TARJETAS - CONCEPTOS EMPRESARIALES")
    print(f"{'=' * 60}{Colores.RESET}")
    print(f"\n{Colores.AMARILLO}Reglas del juego:{Colores.RESET}")
    print("- Responderás 10 preguntas")
    print("- Cada pregunta tiene 4 opciones")
    print("- Necesitas 5 aciertos para aprobar")
    print("- ¡Buena suerte!\n")
    input(f"{Colores.MAGENTA}Presiona ENTER para comenzar...{Colores.RESET}")
    print("\n")

def generar_pregunta_concepto_a_definicion(concepto_correcto, definicion_correcta, todos_conceptos):
    """Genera una pregunta mostrando la definición y pidiendo el concepto"""
    print(f"{Colores.AZUL}DEFINICIÓN:{Colores.RESET} {definicion_correcta}\n")
    
    # Crear lista de opciones (3 incorrectas + 1 correcta)
    opciones_incorrectas = random.sample([c for c in todos_conceptos if c != concepto_correcto], 3)
    opciones = opciones_incorrectas + [concepto_correcto]
    random.shuffle(opciones)
    
    # Mostrar opciones
    for i, opcion in enumerate(opciones, 1):
        print(f"{Colores.BLANCO}{i}. {opcion}{Colores.RESET}")
    
    return opciones.index(concepto_correcto) + 1

def generar_pregunta_definicion_a_concepto(concepto_correcto, definicion_correcta, todas_definiciones):
    """Genera una pregunta mostrando el concepto y pidiendo la definición"""
    print(f"{Colores.AZUL}CONCEPTO:{Colores.RESET} {Colores.NEGRITA}{concepto_correcto}{Colores.RESET}\n")
    
    # Crear lista de opciones (3 incorrectas + 1 correcta)
    opciones_incorrectas = random.sample([d for d in todas_definiciones if d != definicion_correcta], 3)
    opciones = opciones_incorrectas + [definicion_correcta]
    random.shuffle(opciones)
    
    # Mostrar opciones (acortadas para mejor visualización)
    for i, opcion in enumerate(opciones, 1):
        opcion_corta = opcion[:80] + "..." if len(opcion) > 80 else opcion
        print(f"{Colores.BLANCO}{i}. {opcion_corta}{Colores.RESET}")
    
    return opciones.index(definicion_correcta) + 1

def jugar():
    """Función principal del juego"""
    mostrar_bienvenida()
    
    # Variables del juego
    aciertos = 0
    preguntas_totales = 10
    
    # Seleccionar 10 conceptos aleatorios para el juego
    conceptos_juego = random.sample(list(conceptos.items()), preguntas_totales)
    
    # Jugar las 10 rondas
    for numero_pregunta in range(1, preguntas_totales + 1):
        print(f"{Colores.CYAN}{'=' * 60}")
        print(f"PREGUNTA {numero_pregunta} de {preguntas_totales}")
        print(f"{'=' * 60}{Colores.RESET}\n")
        
        concepto, definicion = conceptos_juego[numero_pregunta - 1]
        
        # Alternar tipo de pregunta
        if numero_pregunta % 2 == 1:
            # Mostrar definición, pedir concepto
            respuesta_correcta = generar_pregunta_concepto_a_definicion(
                concepto, definicion, list(conceptos.keys())
            )
        else:
            # Mostrar concepto, pedir definición
            respuesta_correcta = generar_pregunta_definicion_a_concepto(
                concepto, definicion, list(conceptos.values())
            )
        
        # Obtener respuesta del usuario
        while True:
            try:
                respuesta_usuario = int(input(f"\n{Colores.AMARILLO}Tu respuesta (1-4): {Colores.RESET}"))
                if 1 <= respuesta_usuario <= 4:
                    break
                else:
                    print(f"{Colores.ROJO}Por favor, ingresa un número entre 1 y 4.{Colores.RESET}")
            except ValueError:
                print(f"{Colores.ROJO}Por favor, ingresa un número válido.{Colores.RESET}")
        
        # Verificar respuesta
        if respuesta_usuario == respuesta_correcta:
            print(f"{Colores.VERDE}{Colores.NEGRITA}✓ ¡CORRECTO!{Colores.RESET}")
            aciertos += 1
        else:
            print(f"{Colores.ROJO}{Colores.NEGRITA}✗ INCORRECTO.{Colores.RESET} La respuesta correcta era la opción {respuesta_correcta}")
        
        print(f"\n{Colores.MAGENTA}Aciertos hasta ahora: {aciertos}/{numero_pregunta}{Colores.RESET}\n")
        
        if numero_pregunta < preguntas_totales:
            input(f"{Colores.MAGENTA}Presiona ENTER para la siguiente pregunta...{Colores.RESET}")
            print("\n")
    
    # Mostrar resultado final
    print("=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)
    print(f"\nAciertos: {aciertos}/{preguntas_totales}")
    print(f"Porcentaje: {(aciertos/preguntas_totales)*100:.1f}%")
    
    if aciertos >= 5:
        print("\n🎉 ¡APROBADO! ¡Felicidades!")
    else:
        print("\n📚 No aprobado. ¡Sigue estudiando!")
    
    print("\n" + "=" * 60)

# Iniciar el juego
if __name__ == "__main__":
    jugar()
