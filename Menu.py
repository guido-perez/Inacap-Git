
from Matricula import Matricula
from Persona import Persona
from Estudiante import Estudiante

import sys

class Menu:
    useraux='' 
    Rut = ''

    #Creacion de Menu con las opciones basicas de seleccion
def Menu():
       
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
        print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧")
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ PRINCIPAL ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n")
        print("1.- Matricularse(Estudiante Nuevo)                                           ") 
        print("2.- Estudiantes                                                          ") # Invoca a la clase Estudiantes se valida por usuario
        print("3.- Docentes                                                             ") # Invoca a la Clase Docentes se valida por usuario
        print("4.- Jefe de Carrera                                                      ") # Invoca a la Clase JefedeCarrera se valida por usuario
        print("5.- Administrador                                                        ") # Salimos del programa
        print("                                                                      ") # Salimos del programa
        print("6.- Salir                                                           ") # Salimos del programa   
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
        print("  Todos los derechos e izquierdos reservados®   ")
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
    
    
op=0
while not op == 6:
        
        Menu()
        op=int(input("✧ Seleccione una opcion: "))
        
        if op > 0 and op <= 5:
            #se cumplan ambas opciones
            if op == 1: #Inicio Matricula
                    print("\n✦ Accediendo al Portal Matriculas\n")
                    Mat = Matricula()
                    Mat.MostrarCarrera()
                    Mat.CalcularCuota()
                    Mat.ingresarMatricula()
                    Mat.Transaccion() 
                
                   
            #Fin Matricula
            if op == 2: #Inicio Estudiante
                 
                useraux = 'Estudiante'
                Rut = input("\nIngrese Rut para validar usuario:")
                User = Persona()
                User.Validacion(useraux, Rut)
                 
                def MenuEstudiante():
 
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ ESTUDIANTE ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n   ") # Invoca a la Clase Matricula
                    print("1.- Ver Modulos                                                       ") # Invoca a la Funcion verModulos   #OK
                    print("2.- Ver Notas                                                         ") # Invoca a la Funcion verNotas   #OK
                    print("3.- Cambiar contraseña                                                ") # Invoca a la Funcion CambiarContraseña #OK
                    print("4.- Portal de Pago                                                    ") # Invoca a la Funcion ModificarCuponera 
                    print("                                                                      ")
                    print("\n5.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                
                op=0
                while not op == 6:
                        
                        MenuEstudiante()
                        op=int(input("✧ Seleccione una opcion: "))
                        
                        if op > 0 and op <= 4:
                            #se cumplan ambas opciones
                            if op == 1:
                                print("\n✦ Accediendo a Portal Modulos de Estudiante\n")

                                Est = Estudiante() # Instanciar Clase Estudiante para obtener sus funciones
                                Est.verModulos(Rut) # Pasamos por parametros el usuario ya validado, para obtener resultados
                                
                            if op == 2:
                                print("\n✦ Accediendo a Portal Notas de Estudiante\n")
                    
                                Est = Estudiante() # Instanciar Clase Estudiante para obtener sus funciones
                                Est.verNotas(Rut)  # Pasamos por parametros el usuario ya validado, para obtener resultados


                            if op == 3:
                                print("\n✦ Accediendo a Portal Cambiar Contraseña\n")
                                Per = Persona() # Instanciar Clase Persona para obtener sus funciones
                                Per.CambiarContraseña(useraux, Rut) # Pasamos por parametros el usuario ya validado, para obtener resultados
                          
                            if op == 4:
                                print("\n✦ Accediendo a Portal de Pago\n")
                             
                                Mat = Matricula()  # Invocamos Clase Matricula para actualizar la cuponera
                                Mat.ModificarCuponera(Rut) # Pasamos por parametros el usuario ya validado, para obtener resultados

                                
          
                            if op == 5:
                                sys.exit("Saliendo del MunuEstudiante")
                          
                        else:
                            print("\n--- Opcion seleccionada no es valida ---")
                            print("--- Vuelva a seleccionar una de las alternativas del MunuEstudiante --- \n")   
                   
            #Fin Estudiante
            if op == 2:
                
                useraux = 'Docente'
                User = Persona()
                User.Validacion(useraux)  
                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Docente
                
                def MenuDocente():
  
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ DOCENTE ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n      ") # Invoca a la Clase Nota
                    print("1.- Agregar Nota a Estudinte                                          ") # Invoca a la Funcion Agregar Nota
                    print("2.- Modificar Nota a Estudinte                                        ") # Invoca a la Funcion Modificar Nota
                    print("3.- Eliminar Nota a Estudinte                                         ") # Invoca a la Funcion Eliminar Nota
                    print("4.- Cambiar contraseña                                                ") 
                    print("                                                                      ") 
                    print("6.-                                                                   ")
                    print("\n4.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                
                op=0
                while not op == 4:
                        
                        MenuDocente()
                        op=int(input("✧ Seleccione una opcion: "))
                        
                        if op > 0 and op <= 4:
                            #se cumplan ambas opciones
                            if op == 1:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 2:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 3:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 4:
                                print("\n✦ Accediendo a Portal Cambio de Contraseña\n")
                                useraux = 'Docente'
                                User = Persona()
                                User.CambiarContraseña(useraux)

                                # Invocamos Clase Persona modificar la contraseña para ver ver notas
                            if op == 5:
                                sys.exit("Saliendo del MenuDocente")
                                
                        else:
                            print("\n--- Opcion seleccionada no es valida ---")
                            print("--- Vuelva a seleccionar una de las alternativas del MenuDocente --- \n")   

            #Fin Docentes
            if op == 3:
                
                useraux = 'JefeCarrera'
                User = Persona()
                User.Validacion(useraux)  
                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Jefe de Carrera
                
                def MenuJefeCarrera():
                    
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧            ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ JEFE DE CARRERA ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n") # Invoca a la Clase Nota
                    print("1.- Asignar Modulo a Estudinte                                      ") # Invoca a la Funcion Agregar Nota
                    print("2.- Modificar Modulo a Estudinte                                      ") # Invoca a la Funcion Modificar Nota
                    print("3.- Eliminar Modulo a Estudinte                                       ") # Invoca a la Funcion Eliminar Nota
                    print("4.- Ver Modulos del Sistema                                           ") 
                    print("5.- Nuevo Modulo                                                      ")                     
                    print("6.- Modificar Modulo                                                  ") 
                    print("7.- Eliminar Modulo                                                   ")
                    print("8.- Agregar Modulo a Docente                                          ") 
                    print("9.- Modificar Modulo a Docente                                        ")                      
                    print("10.- Eliminar Modulo a Docente                                        ") 
                    print("11.- Ver Modulos del Sistema                                          ") 
                    print("12.- Cambiar contraseña                                               ") 
                    print("                                                                      ")                                                            
                    print("\n13.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                
                op=0
                while not op == 12:
                        
                        MenuJefeCarrera()
                        op=int(input("✧ Seleccione una opcion: "))
                        
                        if op > 0 and op <= 12:
                            #se cumplan ambas opciones
                            if op == 1:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 2:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 3:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 4:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 5:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 6:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 7:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 8:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 9:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 10:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 11:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")                                 
                            if op == 12:
                                print("\n✦ Accediendo a Portal Cambio de Contraseña\n")
                                useraux = 'Jefe Carrera'
                                User = Persona()
                                User.CambiarContraseña(useraux)                               
                            if op == 13:
                                sys.exit("Saliendo del MenuDocente")
                        else:
                            print("\n--- Opcion seleccionada no es valida ---")
                            print("--- Vuelva a seleccionar una de las alternativas del MenuDocente --- \n")   

            #Fin JefeCarrera
            if op == 4:
                print("\nAccediento al Formulario Administrador\n")
                useraux = 'Administrador'
                User = Persona()
                User.Validacion(useraux)
                
                def MunuAdmin():
                    
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧            ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ ADMIN ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n") # 
                    print("1.- Ingresar Usuarios                                                ") # 
                    print("2.- Eliminar Usuarios                                                ") # Invoca a la funcion Eliminar Usuarios
                    print("3.- Cambiar Contraseña de Usuario                                    ")
                    print("4.- Cambiar Contraseña de Usuario                                    ")
                    print("5.- Ver Estudiantes Matriculados                                     ")
                    print("6.- Matricular                                                       ") # Invoca a la funcion Eliminar Usuarios                    
                    print("7.- Anular Matricula                                                 ") # Invoca a la funcion Anular Matricula Usuarios
                    print("8.- Modificar Matricula                                              ") # a la funcion Modificar Matricula Usuarios
                    print("9.- Ver Notas de Estudiante                                          ") # Invoca a la Funcion VerNota                    
                    print("10.- Agregar Nota a Estudinte                                          ") # Invoca a la Funcion Agregar Nota
                    print("11.- Modificar Nota a Estudinte                                        ") # Invoca a la Funcion Modificar Nota
                    print("12.- Eliminar Nota a Estudinte                                         ") # Invoca a la Funcion Eliminar Nota 
                    print("13.- Ver Modulos de Estudiante                                         ") # Invoca a la Funcion ListaModulos                   
                    print("14.- Inscribir Modulo a Estudinte                                      ") # Invoca a la Funcion Agregar Nota
                    print("15.- Modificar Modulo a Estudinte                                      ") # Invoca a la Funcion Modificar Nota
                    print("16.- Eliminar Modulo a Estudinte                                       ") # Invoca a la Funcion Eliminar Nota
                    print("17.- Ver Modulos del Sistema                                           ") 
                    print("18.- Nuevo Modulo                                                      ")                     
                    print("19.- Modificar Modulo                                                  ") 
                    print("20.- Eliminar Modulo                                                   ")
                    print("21.- Agregar Modulo a Docente                                          ") 
                    print("22.- Modificar Modulo a Docente                                        ")                      
                    print("23.- Eliminar Modulo a Docente                                        ") 
                    print("24.- Ver Modulos de Docente                                          ") 
                    print("                                                                    ")                                                            
                    print("\n25.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    
                op=0
                while not op == 24:
                                            
                    MunuAdmin()
                    op=int(input("✧ Seleccione una opcion: "))
                                            
                    if op > 0 and op <= 24:
                                #se cumplan ambas opciones
                                    if op == 1:
                                        print("\nIngresando Formulario de Ingreso de Usuarios\n")        
                                        User = Persona()
                                        User.ingresoUsuario()
                                        break
                                        # Invocamos a clase Personas
                                        # Invocamos la funcion para ingresar Docente o Jefe de Carrera

                                    if op == 2:
                                        print("\nIngresando Formulario de Eliminar de Usuarios\n")
                                        User = Persona()
                                        User.eliminarDocente()
                                        break

                                        # Invocamos a clase Personas
                                        # Incocamosla funcion para eliminar  Docente o Jefe de Carrera
                                                    
                                    if op == 3:
                                        print("\n✦ Accediendo a Portal Cambio de Contraseña\n")
                                        useraux = 'Administrador'
                                        User = Persona()
                                        User.CambiarContraseña(useraux)     

                                    if op == 4:
                                        pass
                                        
                                    if op == 5:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 6:
                                        print("\nIngresando Formulario de Anular Matricula\n")
                                        User = Matricula()
                                        User.AnularMatricula()
                                        break
                                        # Invocamos a clase personas para validar usuario y contraseña
                                        # Incocamos Clase Persona
                                        
                                    if op == 7:
                                        print("\nIngresando Formulario de Modificar Matricula\n")
                                        User = Matricula()
                                        User.ActualizarMatricula()
                                                                          
                                    if op == 8:
                                        print("Menu en construccion vuelva mas tarde.... ")
                                    if op == 9:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 10:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 11:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 12:
                                        print("Menu en construccion vuelva mas tarde.... ")                                          
                                    if op == 13:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 14:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 15:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 16:
                                        print("Menu en construccion vuelva mas tarde.... ")                                          
                                    if op == 17:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 18:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 19:
                                        print("Menu en construccion vuelva mas tarde.... ")                                          
                                    if op == 20:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 21:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 22:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 23:
                                        print("Menu en construccion vuelva mas tarde.... ") 
                                    if op == 24:
                                        print("Menu en construccion vuelva mas tarde.... ")                                                                                      
                                    if op == 25:
                                        sys.exit("Saliendo del MunuAdmin")
                                                
                    else:
                                print("\n--- Opcion seleccionada no valida ---")
                                print("--- Vuelva a seleccionar una de las alternativas del MenuAdmin --- \n")
                                                
                
            if op == 5:
                sys.exit("Saliendo del sistema")
            
        else:
            print("\n--- Opcion seleccionada no valida ---")
            print("--- Vuelva a seleccionar una de las alternativas del MenuAdmin --- \n")

            



                

