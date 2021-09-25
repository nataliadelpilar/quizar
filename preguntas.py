import json
import json
import random

import pandas as pd

# con esta funcion se realiza la seleccion de preguntas aleatoriamente dependiendo de su nivel
def generador_preguntas():
    vnivel =1
    preguntasCategory = ["", "", "", "", ""]
    respuesta1=[]
    respuesta2=[]
    respuesta3=[]
    respuesta4=[]
    respuesta5=[]
    respuestacategory=[respuesta1,respuesta2,respuesta3,respuesta4,respuesta5]
    while vnivel<6:
        with open('preguntas.json',encoding='utf-8') as file:
              a=json.load(file)
              data=pd.DataFrame(a)

              nivel = data.query(f'nivel=="{vnivel}"')
              preguntaSelecionada = nivel.sample()
              respuestas=[(preguntaSelecionada.correcta.values[0],True),
                         (preguntaSelecionada.incorecta_1.values[0],False),
                         (preguntaSelecionada.incorrecta_2.values[0],False),
                         (preguntaSelecionada.incorrecta_3.values[0],False)
                         ]

              random.shuffle(respuestas)
              #print(preguntaSelecionada.pregunta.values[0])
              #print(respuestas)

              if vnivel==1:

                  preguntasCategory[0]=preguntaSelecionada.pregunta.values[0]
                  respuestacategory[0]=respuestas

                  #print(preguntasCate)
                  #print(respuestacategory[0])
                  vnivel=vnivel+1

              elif vnivel==2:
                 preguntasCategory[1] = preguntaSelecionada.pregunta.values[0]
                 respuestacategory[1] = respuestas
                 #print(preguntasCate)
                 #print(respuestacategory[1])
                 vnivel = vnivel + 1

              elif vnivel == 3:
                 preguntasCategory[2] = preguntaSelecionada.pregunta.values[0]
                 respuestacategory[2] = respuestas
                 #print(preguntasCate)
                 #print(respuestacategory[2])
                 vnivel = vnivel + 1

              elif vnivel == 4:
                 preguntasCategory[3] = preguntaSelecionada.pregunta.values[0]
                 respuestacategory[3] = respuestas
                 #print(preguntasCate)
                 #print(respuestacategory[3])
                 vnivel = vnivel + 1

              elif vnivel == 5:
                 preguntasCategory[4] = preguntaSelecionada.pregunta.values[0]
                 respuestacategory[4] = respuestas

                 #print(respuestacategory)
                 #print(preguntasCategory)
                 vnivel = vnivel + 1

              else:

                  break


    return  (preguntasCategory,respuestacategory)