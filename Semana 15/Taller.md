# 🧩 Semana 15: Taller de Práctica de Gestión de Incidentes

**Curso:** Gestión de Tecnologías de la Información  
**Docente:** Dr. Oscar Jimenez Flores  
[CTI Vitae Concytec](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)  
[LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/)

---

## 🎯 Objetivo

Aplicar la práctica de **Gestión de Incidentes** de ITIL 4 para garantizar la restauración eficiente de servicios TI ante interrupciones, mediante el diseño de un procedimiento de atención, priorización y documentación de incidentes relacionados con el servicio TI desarrollado en clase.

- **Duración:** 90 minutos  
- **Modalidad:** Presencial (X)    Virtual ( )  
- **Integrantes por grupo:** 4 estudiantes  
- **Producto final:** Informe académico + presentación oral

---

## 🔍 Fases del Taller

1. **Identificar posibles incidentes**  
   A partir del servicio TI trabajado, plantear al menos 6 situaciones que impliquen interrupciones o degradación del servicio.

2. **Clasificar y priorizar incidentes**  
   Usar criterios como impacto, urgencia y frecuencia para definir prioridad.

3. **Diseñar el proceso de atención**  
   Describir cómo será registrado, asignado y atendido cada tipo de incidente. Incluir flujos, responsables y herramientas.

4. **Proponer medidas de mejora**  
   Con base en los incidentes, sugerir acciones para prevenir su recurrencia o disminuir su impacto.

---

## 📘 Informe Académico

El informe debe mostrar cómo la gestión de incidentes contribuye a mantener el valor y disponibilidad del servicio. Debe tener un **mínimo de 4 páginas** y ser subido por un integrante al aula virtual.

> ⚠️ No se aceptarán informes sin vínculo directo con el servicio TI del grupo.

### ✍️ Estructura sugerida del informe

1. **Carátula**  
   Título del taller, nombre del servicio TI, carrera, docente y nombres completos de los integrantes.

2. **Descripción del servicio TI**  
   Breve descripción del proceso o sistema trabajado.

3. **Listado y análisis de incidentes**  
   Tabla con al menos 4 incidentes posibles según el servicio de TI que viene desarrollando.

4. **Procedimiento de gestión de incidentes**  
   Incluir flujograma o descripción detallada de pasos desde la detección hasta la resolución, con tiempos estimados.

5. **Propuesta de mejora**  
   Acciones preventivas o correctivas basadas en el análisis de los incidentes.

6. **Conclusión**  
   Reflexión sobre la importancia de gestionar incidentes de forma estructurada.

---

## 🛠 Consideraciones

1. Se espera que el grupo diseñe un proceso **claro y aplicable**.  
2. Incluir gráficos (flujos, diagramas, etc.) si fortalecen la explicación.

---

## 🧾 Criterios de Evaluación

| Criterio                                               | Puntaje |
|--------------------------------------------------------|---------|
| Identificación y análisis de incidentes                | 5 pts   |
| Diseño del proceso de atención de incidentes           | 10 pts  |
| Presentación oral del grupo                            | 5 pts   |
| **Total**                                              | **20**  |

---

## 📥 Entrega

- **Informe en PDF:** subir al Aula Virtual hasta la fecha indicada por el docente.  
- **Exposición presencial:** 10 minutos por grupo con preguntas del docente.

---

## 📄 Ejemplo de Tablas

### Tabla 1: Análisis de Incidentes

| **ID**     | **Incidente Detectado**                                  | **Causa Probable**                    | **Impacto**                      | **Frecuencia Estimada** | **Prioridad** | **Módulo Afectado**       |
|------------|----------------------------------------------------------|--------------------------------------|----------------------------------|--------------------------|----------------|----------------------------|
| INC-BNK-01 | Transferencias interbancarias fallidas                   | Fallo en API externa del proveedor   | Alta: impide operaciones clave   | 3 veces por semana       | Alta           | Transferencias             |
| INC-BNK-02 | App se cierra al ingresar al módulo de inversiones       | Error de memoria en versión Android  | Media: afecta solo a cierto perfil | 1 vez por semana        | Media          | Inversiones                |
| INC-BNK-03 | Notificaciones push no llegan al usuario final           | Configuración errónea del backend    | Media: afecta comunicación       | Diaria                   | Media          | Notificaciones             |
| INC-BNK-04 | Error al escanear DNI para apertura de cuenta            | Fallo en reconocimiento OCR          | Alta: afecta onboarding de nuevos clientes | 2 veces por semana | Alta           | Registro de nuevos clientes |



### Tabla 2: Procedimiento de Gestión de Incidentes

| **ID de Incidente** | **Paso** | **Actividad**                                                       | **Responsable**             | **Herramienta/Tecnología**        | **Tiempo Estimado** |
|---------------------|----------|----------------------------------------------------------------------|------------------------------|------------------------------------|----------------------|
| INC-BNK-01          | 1        | Registro automático vía monitoreo de logs                           | DevOps / Infraestructura     | Splunk + Jira                      | Inmediato            |
|                     | 2        | Escalamiento a soporte por criticidad del servicio                  | Coordinador de Incidentes    | Jira Workflow                      | 15 minutos           |
|                     | 3        | Diagnóstico de integración API y verificación con proveedor externo | Soporte Nivel 2              | Postman + Telnet                   | 1 hora               |
|                     | 4        | Aplicación de hotfix o enrutamiento alterno                         | Dev Backend                  | Docker / Git                       | 2 horas              |
| INC-BNK-02          | 1        | Registro del ticket por usuario desde la app                        | Mesa de Servicio             | Canal App / Helpdesk               | 10 minutos           |
|                     | 2        | Clasificación como incidente funcional (nivel medio)                | Mesa de Servicio             | Formulario ITIL                    | 15 minutos           |
|                     | 3        | Pruebas de replicación en Android                                   | QA                           | Emulator + Firebase Test Lab       | 45 minutos           |
|                     | 4        | Envío a desarrollo para fix                                          | Dev Mobile                   | GitHub Pull Request                | 1 día                |
| INC-BNK-03          | 1        | Alerta generada desde plataforma de monitoreo de notificaciones     | DevOps                       | Firebase Cloud Messaging Logs      | Inmediato            |
|                     | 2        | Validación del estado de FCM y backend                               | Backend                      | Console + Logs                     | 30 minutos           |
|                     | 3        | Reconfiguración de tokens y reinicio de servicios                    | Backend                      | Docker / Redis / PM2               | 1 hora               |
| INC-BNK-04          | 1        | Reporte de usuario al no poder escanear documento                   | Mesa de Servicio             | Portal Web + Captura de pantalla   | 15 minutos           |
|                     | 2        | Validación manual de funcionalidad OCR                              | QA + Frontend                | App Testing / Scanner Module       | 1 hora               |
|                     | 3        | Ajuste en la biblioteca OCR + reentrenamiento del modelo            | Dev Frontend + IA Team       | Tesseract + Dataset DNI            | 1 día                |



### Tabla 3: Acciones Preventivas

| **ID**       | **Acción Propuesta**                                                   | **Responsable Técnico**       | **Riesgo Asociado**                          | **Indicador de Éxito**                                |
|--------------|------------------------------------------------------------------------|-------------------------------|------------------------------------------------|--------------------------------------------------------|
| INC-BNK-01   | Implementar redundancia en la conexión con la API interbancaria        | Equipo de Infraestructura     | Caída del proveedor externo                   | 0 fallos en transferencias durante 2 semanas seguidas |
| INC-BNK-02   | Optimizar consumo de memoria en módulo de inversiones Android          | Líder de Desarrollo Mobile    | App cerrada inesperadamente                    | Crash rate < 0.5% en el módulo                        |
| INC-BNK-03   | Configurar correctamente el servicio de notificaciones push (FCM)      | Dev Backend + DevOps          | Desinformación del usuario                     | +90% de recepción confirmada en dispositivos activos   |
| INC-BNK-04   | Integrar motor OCR más robusto + testeo multiplataforma                | QA Lead + Dev Frontend        | Pérdida de clientes potenciales                | 95% de éxito en escaneo en la primera prueba          |
