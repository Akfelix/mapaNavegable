# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    define e = Character("Personaje 1")
    image trainBG  = Image("trainSeats.jpg") ##Declarado el fondo para poder usarlo mas tarde
    image iglesia = Image("paisaje2.jpg") #Declarado el fondo de la zona "Iglesia"
    image calavera = Image("paisaje.jpg") #Declarado el fondo de la zona "Calavera"
    image pueblo = Image("puebloPaisaje.jpg") #Declarado el fondo de la zona "Pueblo"
    #Las imagenes no tienen la dimensio correcta asi que no se veran bien pero se entiende lo que se pretende hacer creo.


screen mapaMundo:
    imagemap:
        xcenter 0.5 #Esto centra el "screen" entero
        ground "mapaPruebaMundoSinMarcar.png" ##Carga un mapa1 por defecto 
        hover "mapaPruebaMundoMarcado.png" ##Carga un mapa para cuando el usuario pase el cursor por encima
        hotspot(261, 346,341, 422) clicked Return("Iglesia") hovered ShowTransient("the_img2", img="paisaje2V3.png") unhovered Hide("the_img2") #307 x 163 medidas en este caso   
        
        ##Se especifican las coordenadas (con "Shift+D" se puede seleccionar el "Image location picker" para ver las coordenadas de la imagen). Al pinchar en dicha zona devuelve una cadena de texto (Iglesia en este caso) y mas adelante la compara ver que selecciono el usuario

        hotspot(75, 81,167, 165) clicked Return("Pueblo") hovered ShowTransient("the_img3", img="puebloPaisajeV1.png") unhovered Hide("the_img3")  
        
        hotspot (272, 22,363, 104) clicked Return("Calavera") hovered ShowTransient("the_img", img="paisajev2.png") unhovered Hide("the_img")  
        
        ##hovered ShowTransient("the_img", img="paisajev2.png") unhovered Hide("the_img") |||| Este trozo de codigo hace que cuando pase por encima de ese objeto muestre una imagen cuya posicion esta almacenada en el screen de abajo. En esta linea se tiene que indicar que imagen quieres que aparezca


screen the_img(img): #En esta screen se indica donde quieres que aparezca la imagen. Arriba en lo del Hotspot es donde se llama
    add img pos (585, 50)

screen the_img2(img):
    add img pos (355,  415)

screen the_img3(img):
    add img pos (75, 81)


# The game starts here.
## https://namelessdistrict.wordpress.com/2016/12/13/choice-menu-image-mapping/ 
##Probbar el codigo de arriba para hacer un mapa con hotspots
label start:

    scene trainBG
    "Ahora el mapa aparece:"

    call screen mapaMundo with dissolve #Aqui se llamara a la "Screen" que contiene el mapa seleccionable
    
    $ result = _return #Variable que usaremos para comparar la cadena de texto que devuelve el Hotspot al pinchar con los condicionales de abajo y detecta cual hemos pinchado
    
    if result == "Iglesia":
        e "Se eligio la Iglesia"
        "Ahora aqui podriamos poner un jump para cambiar de escena"
        jump destino1
    elif result == "Pueblo":
        e "Pueblo pequeño en el norte"
        jump destino2
        "Ahora aqui podriamos poner un jump para cambiar de escena"
    elif result == "art":
        e "You picked art!"
    elif result == "Calavera":
        e "Zona calavera"
        "Ahora aqui podriamos poner un jump para cambiar de escena"
        jump destino4


label destino1:
    scene iglesia
    with fade
    "Se llego al destino Iglesia"
    return

label destino2:
    scene pueblo
    with fade
    "Se llego al destino Pueblo"
    return

label destino4:
    scene calavera
    with fade
    "Se llego al destino calavera"
    return
