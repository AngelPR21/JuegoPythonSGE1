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
    "BOM": "Lista de materiales. Gestión de los componentes e inventario necesarios para fabricar productos.",
    "BSC": "Cuadro de mando integral. Metodología de gestión estratégica para el seguimiento del plan estratégico mediante indicadores.",
    "Cloud Computing": "Computación en la nube. Servicios de hardware y software proporcionados a través de Internet.",
    "CMS": "Sistema gestor de contenidos orientado a la publicación y gestión de contenidos accesibles mediante servicio web.",
    "Compliance": "Procedimientos que garantizan la observancia y cumplimiento de la normativa interna y la legislación aplicable.",
    "CRM": "Sistema de gestión de las relaciones con los clientes que ayuda en la captación y mantenimiento de la cartera de clientes.",
    "Dashboard": "Panel de control que muestra visualizaciones e indicadores clave (KPI) para monitorizar el rendimiento.",
    "Dataset": "Conjunto estructurado de datos que sirve para análisis, informes o toma de decisiones en la empresa.",
    "Data Analyst": "Profesional encargado de procesar, analizar y transformar datos en información útil para la toma de decisiones.",
    "Data Mining": "Minería de datos. Técnicas orientadas a descubrir patrones y tendencias en grandes bases de datos.",
    "Data Warehouse": "Almacén de datos centralizado que integra información de varias fuentes para análisis y reporting.",
    "DMS": "Sistema de gestión documental orientado a la organización y mantenimiento de la documentación empresarial.",
    "DSS": "Sistema de ayuda a la toma de decisiones que produce información de valor para asistir a la dirección.",
    "Eficacia": "Alcanzar las metas establecidas por la empresa.",
    "Eficiencia": "Lograr las metas utilizando la menor cantidad de recursos posible.",
    "ERP Vertical": "ERP adaptado a las necesidades específicas de un sector o industria, optimizando procesos particulares.",
    "ERP Horizontal": "ERP con funcionalidades generales aplicables a múltiples sectores para cubrir procesos comunes.",
    "ETL": "Procesos de extracción, transformación y carga de datos entre sistemas para integrar información.",
    "Front-Office": "Conjunto de actividades y procesos realizados de cara al cliente.",
    "Granularidad": "Nivel de detalle de los datos; mayor granularidad permite análisis más precisos.",
    "IaaS": "Infraestructura como servicio. Provisión de recursos computacionales (CPU, almacenamiento, redes) bajo demanda.",
    "Insight": "Conocimiento valioso extraído del análisis de datos que apoya decisiones estratégicas.",
    "IoT": "Internet de las cosas. Interconexión de dispositivos electrónicos para recopilar y transmitir datos.",
    "KMS": "Sistema de gestión del conocimiento orientado a documentación, manuales y procedimientos organizacionales.",
    "Know-how": "Conocimientos prácticos y experiencia de una organización que le confieren ventaja competitiva.",
    "KPI": "Indicador clave de rendimiento. Métrica que permite medir magnitudes o áreas de interés.",
    "OLAP": "Bases de datos multidimensionales orientadas al procesamiento analítico de datos empresariales.",
    "On-Premise": "Instalación local de sistemas cuando los servicios y datos se ubican en la propia empresa.",
    "PaaS": "Plataforma como servicio. Entorno en la nube para desarrollar, desplegar y gestionar aplicaciones.",
    "Productividad": "Relación entre los productos obtenidos y los insumos utilizados en un período determinado.",
    "ROI": "Retorno de la inversión. Medida que relaciona el beneficio obtenido con el capital invertido.",
    "SaaS": "Software como servicio. Software accesible mediante suscripción a través de Internet.",
    "SRM": "Gestión de relaciones con proveedores orientada a optimizar la adquisición y colaboración con suministradores.",
    "Trazabilidad": "Capacidad de seguir y documentar el historial y aplicación de un producto, proceso o dato.",
    "Workflow": "Flujo de trabajo. Definición y automatización de procesos para que la información y tareas circulen correctamente."
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
