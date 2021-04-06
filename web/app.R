#
# Aplicación web para la utilización del modelo creado para
# predecir el numero de hijos en un hogar colombiano
#
# Autor: Alejandro Jimenez Franco
# Técnicas en Aprendizaje Estadístico - Semestre 01 2021
# Universidad Nacional de Colombia
#


library(shiny)
source("Modelo.R")

ui <- fluidPage(title = "Predicción número de hijos",
        shinyjs::useShinyjs(),
        tags$style(type="text/css", "body {padding-top: 70px;}"),
        navbarPage("Predicción número de hijos", inverse = TRUE, position = "fixed-top",
          tabPanel("Modelo", 
           
           fluidRow(
            column(8,
                 fluidRow(
                   column(12,
                    tags$p("El siguiente es una aplicación web de un modelo de predicción del numero de hijos en un hogar colombiano, 
                    usando la más reciente encuesta de calidad de vida del DANE (ECV 2019)"),
                    tags$h4("Modo de uso:"),
                    tags$p("Para usarla debe rellenar los campos o selectores que se observan a continuación y luego presionar el botón de enviar datos"),
                    tags$p("Las opciones deben ser rellenadas con la información del hogar y del Jefe del hogar")
                   )
                 ),
                fluidRow(
                 column(12,
                    sliderInput(inputId = "edadJefe", width = "100%",
                                label = "Edad del jefe del hogar",
                                value = 30, min = 12, max = 110),
                  )
                ),
                fluidRow(
                 column(12,
                    sliderInput(inputId = "cantPersonas", width = "100%",
                                label = "Cantidad de personas en el hogar",
                                value = 4, min = 1, max = 20)
                 )
                ),
                fluidRow(
                  column(6,
                     numericInput(inputId = "ingresosTotales", width = "100%",
                                  label = "Ingresos del hogar al mes",
                                  value = 600000, min = 0)
                  
                  ),
                  column(6,
                     numericInput(inputId = "valorElectricidad", width = "100%",
                                  label = "Valor que se paga por eléctricidad al mes en el hogar",
                                  value = 100000, min = 0)
                  )
                ),
                fluidRow(
                  column(6,
                     radioButtons(inputId = "sexoJefe", width = "100%",
                                  label = "Sexo del jefe del hogar", 
                                  choices = c("Hombre" ="1",
                                              "Mujer" = "2"))
                  ),
                  column(6,
                     selectInput(inputId = "eduJefe", width = "100%",
                                 label = "Nivel educativo que alcanzo el jefe del hogar", 
                                 choices = c("No estudio" ="0",
                                             "Educacion basica" = "1",
                                             "Educacion profesional no completa" = "2",
                                             "Educacion profesional" = "3")),
                  )
                ),
                fluidRow(
                  column(6,
                     selectInput(inputId = "trabajoJefe", width = "100%",
                                 label = "Dedicación del jefe del hogar", 
                                 choices = c("Trabajando" ="1",
                                             "Buscando trabajo" = "2",
                                             "Estudiando" = "3",
                                             "Oficios del hogar" = "4",
                                             "Incapacitado permanentemente para trabajar" = "5",
                                             "Otra actividad" = "6"))
                         
                  ),
                  column(6,
                     radioButtons(inputId = "usoTecnologia", width = "100%",
                                  label = "Frecuencia de uso de el internet del deje del hogar", 
                                  choices = c("No usa internet" ="0",
                                              "Poco uso del internet" = "1",
                                              "Usa mucho el internet" = "2"))
                         
                  )
                ),
                fluidRow(
                  column(12,
                     selectInput(inputId = "tipoUnion", width = "100%",
                                 label = "Tipo de unión", 
                                 choices = c("No está casado(a) y vive en pareja hace menos de dos años" ="1",
                                             "No está casado(a) y vive en pareja hace dos años o más" = "2",
                                             "Está viudo(a)" = "3",
                                             "Está separado(a) o divorciado(a)" = "4",
                                             "Está soltero(a)" = "5",
                                             "Está casado(a)" = "6"))
                         
                  )
                ),
              
              actionButton(inputId = "enviar", width = "100%",
                           label = "Enviar datos",
                           class = "btn-success"),
              
              textOutput("text")
            ),
          ),
  mainPanel(
    plotOutput('plot1')
  )),
  tabPanel("Enlaces", "tab 2")
),
  
)

server <- function(input, output) {
  
  observeEvent(input$enviar, {
    
    # print(input$edadJefe)
    # print(input$cantPersonas)
    # print(input$ingresosTotales)
    # print(input$valorElectricidad)
    # print(input$sexoJefe)
    # print(input$tipoUnion)
    # print(input$trabajoJefe)
    # print(input$usoTecnologia)
    # print(input$eduJefe)
    
    df = data.frame(list(Sexo.Jefe= input$sexoJefe,
                          Tipo.Union = input$tipoUnion,
                          Trabajo.Jefe = input$trabajoJefe,
                          Uso.tecnologia.Jefe = input$usoTecnologia,
                          Edu.Jefe = input$eduJefe,
                          Edad.Jefe = input$edadJefe,
                          Cantidad.de.personas = input$cantPersonas,
                          Ingresos.totales = input$ingresosTotales,
                          Valor.Electricidad = input$valorElectricidad))
    prediccion <- generar_prediccion(df)
    
    print(prediccion)
    
    withCallingHandlers({
      shinyjs::html(id = "text", html = "")
      warning(prediccion[[2]])
      if (is.null(prediccion[[1]])) {
        warning(prediccion[[2]])
      }
      
    },
    message = function(m) {
      shinyjs::html(id = "text", html = m$message, add = TRUE)
    },
    warning = function(m) {
      shinyjs::html(id = "text", html = m$message, add = TRUE)
    })
    
  })
}

shinyApp(ui = ui, server = server)