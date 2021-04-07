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
        # Algunos cambios en el css de algunos elementos
        tags$head(
          tags$style(type="text/css", "body {padding-top: 70px;}"),
          tags$style(type="text/css","#imagen img {max-width: 100%; width: 100%; height: auto; max-height: 100%}"),
          tags$style("#texto_hijos{
                                 font-size: 20px;
                                 font-style: bold;
                                 text-align: center;
                                 }"),
          tags$style(HTML("hr {border-top: 1px solid #000000;}"))
        ),
        # Navegacion
        navbarPage("Predicción número de hijos", inverse = TRUE, position = "fixed-top",
                   
          # Tab Modelo
          tabPanel("Modelo",
           fluidRow(
            column(8,
                # Descripcion
                wellPanel(
                 fluidRow(
                   column(12,
                    tags$p("La siguiente es una aplicación web de un modelo de predicción del numero de hijos en un hogar colombiano, 
                    usando la más reciente encuesta de calidad de vida del DANE (ECV 2019)."),
                    tags$h4("Modo de uso:"),
                    tags$p("Para usarla debe rellenar los campos o caracteristicas que se observan a continuación y luego presionar el botón de enviar datos"),
                    tags$p("Las opciones deben ser rellenadas con la información del hogar y del Jefe del hogar.")
                   )
                 ),
                ),
                
                # Campos a rellenar
                wellPanel(
                tags$h3("Características"),
                fluidRow(
                 column(12,
                    sliderInput(inputId = "edadJefe", width = "100%",
                                label = "Edad de la persona",
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
                                  label = "Valor que se paga por eléctricidad al mes",
                                  value = 100000, min = 0)
                  )
                ),
                fluidRow(
                  column(6,
                     radioButtons(inputId = "sexoJefe", width = "100%",
                                  label = "Sexo de la persona", 
                                  choices = c("Hombre" ="1",
                                              "Mujer" = "2"))
                  ),
                  column(6,
                     selectInput(inputId = "eduJefe", width = "100%",
                                 label = "Nivel educativo maxima alcanzado por la persona", 
                                 choices = c("No estudio" ="0",
                                             "Educacion basica" = "1",
                                             "Estudios superiores no completos" = "2",
                                             "Estudios superiores completos" = "3")),
                  )
                ),
                fluidRow(
                  column(6,
                     selectInput(inputId = "trabajoJefe", width = "100%",
                                 label = "Principal dedicación de la persona", 
                                 choices = c("Trabajando" ="1",
                                             "Buscando trabajo" = "2",
                                             "Estudiando" = "3",
                                             "Oficios del hogar" = "4",
                                             "Incapacitado permanentemente para trabajar" = "5",
                                             "Otra actividad" = "6"))
                         
                  ),
                  column(6,
                     radioButtons(inputId = "usoTecnologia", width = "100%",
                                  label = "Frecuencia de uso de el internet de la persona", 
                                  choices = c("No usa internet" ="0",
                                              "Poco uso del internet" = "1",
                                              "Usa mucho el internet" = "2"))
                         
                  )
                ),
                fluidRow(
                  column(12,
                     selectInput(inputId = "tipoUnion", width = "100%",
                                 label = "Tipo de unión o estado civil de la persona", 
                                 choices = c("No está casado(a) y vive en pareja hace menos de dos años" ="1",
                                             "No está casado(a) y vive en pareja hace dos años o más" = "2",
                                             "Está viudo(a)" = "3",
                                             "Está separado(a) o divorciado(a)" = "4",
                                             "Está soltero(a)" = "5",
                                             "Está casado(a)" = "6"))
                         
                  )
                ),
              
              # Boton de enviar
              actionButton(inputId = "enviar", width = "100%",
                           label = "Enviar datos",
                           class = "btn-success"),
              
              )
            ),
            
            # Espacio para el resultado
            column(4,
                   fluidRow(
                     wellPanel(
                       tags$h3("Resultado"),
                       imageOutput("imagen"),
                       hr(),
                       textOutput("texto_hijos")
                     )
                   )
               
            )
          ),
  ),
  
  # Espacio de enlaces 
  tabPanel("Enlaces",
     tags$h4("Enlace al reporte técnico"),
     tags$a(href="https://rpubs.com/Alexitouno19/TAE-01-NatalidadColombia", icon("book"), "Reporte técnico", class = "btn btn-primary"),
     tags$h4("Enlace al respositorio del proyecto"),
     tags$a(href="https://github.com/juanescendales/TAE-01-NatalidadColombia", icon("github"), "Repositorio del proyecto", class = "btn", style = "background-color:#000000; color:#ffffff;"),
     hr(),
     # Referencia a los iconos usados con los hijos
     HTML('<div>Iconos diseñados por <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.es/" title="Flaticon">www.flaticon.es</a></div>')
  )
),
  
)

server <- function(input, output) {
  
  # Acciones a ejecutar al momento de presionar enviar
  observeEvent(input$enviar, {
    
    
    # Creo un dataframe con los datos de los campos de la ui, para ser usados posteriormente en la prediccion del modelo
    df = data.frame(list(Sexo.Jefe= input$sexoJefe,
                          Tipo.Union = input$tipoUnion,
                          Trabajo.Jefe = input$trabajoJefe,
                          Uso.tecnologia.Jefe = input$usoTecnologia,
                          Edu.Jefe = input$eduJefe,
                          Edad.Jefe = input$edadJefe,
                          Cantidad.de.personas = input$cantPersonas,
                          Ingresos.totales = input$ingresosTotales,
                          Valor.Electricidad = input$valorElectricidad))
    
    # Genero la prediccion
    prediccion <- generar_prediccion(df)
    
    # Texto para mostrar el numero de hijos
    texto = "hijos"
    if(prediccion[[1]] == 1){
      texto = "hijo"
    }
    
    # Cancateno hijo o hijos segun sea el caso
    textoMostrar = paste(prediccion[[1]], texto, sep=" ")
    
    
    # En caso de que sea la respuesta NULL, mostrare el mensaje de error
    if(is.null(prediccion[[1]])){
      textoMostrar = prediccion[[2]]
    }
    
    
    # Muestro el mensaje en la ui
    output$texto_hijos <- renderText({
      textoMostrar
    })
    
    # Imagen de numero de hijos
    output$imagen <- renderImage({
      
      # Dependiendo del numero de hijos en la prediccion muestro cierta imagen
      filename <- normalizePath(file.path('./img', paste(prediccion[[1]], '.png', sep='')))
      
      # En caso de error muestro una imagen de error
      if(is.null(prediccion[[1]])){
        filename <- normalizePath(file.path('./img/error.png'))
      }
      
      # Retorno una lista con la informacion de la imagen
      list(src = filename,
           contentType = 'image/png',
           width = 400,
           height = 400,
           alt = "Cantidad hijos")
    }, deleteFile = FALSE)
    
  })
}


# Funcionamiento de la app
shinyApp(ui = ui, server = server)