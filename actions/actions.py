
from codecs import utf_7_encode
from typing import Any, Text, Dict, List

from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker, Action, FormValidationAction
from rasa_sdk.events import SlotSet, EventType, UserUtteranceReverted, ConversationPaused, SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

    
from db.db import *

import logging
import re
import unidecode

logger = logging.getLogger(__name__)

#class ActionTriggerResponseSelector(Action):
#    """Returns the chitchat utterance dependent on the intent"""
#
#    def name(self) -> Text:
#        return "action_trigger_response_selector"
#
#    def run(
#        self,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> List[EventType]:
#        retrieval_intent = tracker.get_slot("retrieval_intent")
#        print('retrieval_intent:', retrieval_intent)
#        if retrieval_intent:
#            dispatcher.utter_message(response = f"utter_{retrieval_intent}")
#        
#        return [SlotSet("retrieval_intent", None)]


# class ActionTriggerResponseSelectorFallback(Action):
#     """Returns the chitchat utterance dependent on the intent"""
# 
#     def name(self) -> Text:
#         return "action_trigger_response_selector_fallback"
# 
#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> List[EventType]:
#         retrieval_intent = tracker.get_slot("retrieval_intent")
#         print('retrieval_intent:', retrieval_intent)
 #        if retrieval_intent:
 #            dispatcher.utter_message(response = f"utter_{retrieval_intent}")
 #        
  #       return [SlotSet("retrieval_intent", None)]

class ActionTriggerMenuAnterior(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_trigger_menu_anterior"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        topic = tracker.get_slot("topic")
        print('topic:', topic)
        if topic:
            dispatcher.utter_message(response = f"utter_formulario_{topic}")
        
        return []
class ActionDefaultAskAffirmation(Action):
    def name(self):
            return "action_default_ask_affirmation"
    
    async def run(self, dispatcher, tracker, domain):
        # select the top three intents from the tracker        
        # ignore the first one -- nlu fallback
        ## usar response_selector
        # A prompt asking the user to select an option
        best_intent = tracker.latest_message["intent_ranking"][1]['name']

        flow_intents = ['despedida', 'saludo','agradecimiento', 'ayuda', 'denegar_mas_ayuda', 'confirmar_requerir_mas_ayuda']
        
        if best_intent not in flow_intents:
            message = "Deseas saber,"
        else:
            message = "Quisiste decir,"

        # a mapping between intents and user friendly wordings
        intent_mappings = {
            "despedida": "Adios",
            "saludo": "Hola",
            "agradecimiento": "Gracias",
            "ayuda": "ayuda",
            "denegar_mas_ayuda":"No, eso es todo",
            "confirmar_requerir_mas_ayuda": "Sí, tengo otra consulta mas",
            "matricula_procedimiento": '¿Cuál es proceso de matricula?',
            "matricula__procedimiento_alumno_regular": 'Cuál es el proceso de matrícula para un alumno regular?',
            "matricula__procedimiento_alumno_ingresante":"¿Cuál es el proceso de matrícula para un alumno ingresante?",
            "carnet_universitario__solicitud":"¿Cómo obtener mi carnet universitario?",
            "matricula__cronograma":"¿Cuando es la matrícula?",
            "matricula__horarios":"¿Cuál es mi horario de matrícula?",
            "pago_autoseguro__fechas":"¿Cuando se puede pagar el autoseguro?",
            "pago_autoseguro_procedimiento":"¿Como realizo el pago de autoseguro?",
            "pago_autoseguro__fuera_fecha":"¿Que sucede si demore en realizar el pago de autoseguro?",
            "perdida_turno_matricula":"¿Como puedo matricularme si perdí mi turno de matricula?",
            "matricula_rezagada__procedimiento":"¿Cuál es el procedimiento para la matricula rezagada?",
            "cambio_seccion":"¿Cuál es procedimiento para hacer un cambio de sección?",
            "cursos_horarios":"¿Donde puedo ver los horarios de los cursos de este ciclo?",
            "retiro_parcial__fechas":"¿En que semana se realiza el retiro parcial?",
            "retiro_parcial__procedimiento":"¿Cómo realizo un retiro parcial?",
            "retiro_parcial__unico_curso":"¿El retiro parcial aplica para los estudiantes que llevan solo un curso?",
            "retiro_parcial__maximo_cursos":"¿Cuantos cursos es el máximo que puedo retirarme?",
            "retiro_total__fechas":"¿En que fecha se realiza el retiro total?",
            "retiro_total__requisitos_documentos_justificacion":"¿Es necesario justificar con documentos el motivo de retiro total?",
            "retiro_total__motivos_procede":"¿Cuáles son los motivos para acceder al retiro total?",
            "retiro_total__formato_solicitud":"¿Cuál es el modelo para la solicitud de retiro total?",
            "retiro_total__procedimiento":"¿Cómo hago el retiro total de mis cursos?",
            "reserva_matricula__procedimiento":"¿Cómo reservo mi matricula?",
            "reserva_matricula__fechas":"¿Hasta que dias puedo enviar la solicitud de reserva de matricula ?C",
            "reserva_matricula__formato_solicitud":"¿Cuál es el modelo de solicitud para la reserva de matricula?",
            "reincorporacion__procedimiento":"¿Cuál es el procedimiento para solicitar reincorporación?",
            "reincorporacion_rezagada__procedimiento":"Si ya pasaron las fechas de reincoporacion, ¿Puedo enviar mi solicitud de reincoporacion?",
            "reincorporacion__fechas":"¿Hasta cuando enviar mi solicitud de reincorporacion?",
            "reincorporacion__costo":"¿Cuánto se paga por el tramite de reincorporación?",
            "reincorporacion__formato_solicitud":"¿Hay un modelo para la solicitud de reincorporación?",
            "constancia_matricula__solicitud_procedimiento":"¿Cómo puedo obtener una constancia de matricula?",
            "constancia_matricula__pago":"¿Cuánto se paga por la Constancia de Matrícula?",
            "constancia_matricula__formato_solicitud":"¿Hay un modelo para la solicitud de constancia de matricula?",
            "constancia_de_notas__procedimiento":"¿Como solicitar una constancia de notas?",
            "constancia_de_notas__formato_solicitud":"¿Hay algun modelo para la solicitud de constancia de notas?",
            "constancia_de_estudios__formato_solicitud":"¿Hay algún modelo para la solicitud de constancia de estudios?",
            "constancia_de_estudios__procedimiento":"¿Cómo solicitar una constancia de estudios?",
            "horario_atencion_aera":"¿Cuál es el horario de AERA?",
            "solicitud_correo_institucional_procedimiento":"¿Cómo solicito mi correo UNI?",
            "retiro_parcial__cursos_repetidos": "¿Es posible retirarme de un curso que haya repetido?",
            'formato_solicitud': "¿Cuál es el modelo para la solicitud?",
            'costo_tramite': "¿Cuanto es el costo por el tramite?",
            'pago_fechas': "¿Hasta cuando puedo realizar el pago?",
            'procedimiento_tramites_fechas': "¿Cuando puedo realizar el procedimiento o tramite?",
        }

       
        best_intent = tracker.latest_message["intent_ranking"][1]['name']
        
        if best_intent == 'faq':
            sub_intent = tracker.latest_message['response_selector']['faq']['ranking'][0]['intent_response_key']
            # best_intent = sub_intent
            message = "Deseas saber,"
            title_intent = intent_mappings[sub_intent]
            paylod = f'/trigger_response_selector{{{{"retrieval_intent": "{sub_intent}"}}}}'
            print(paylod)

        else: 
            message = "Quisiste decir,"
            title_intent = intent_mappings[best_intent]
            paylod = "/{}".format(best_intent)
      
        buttons = [
            {
                "title": 'Si',
                "payload": paylod
            },
            {
            "title": "No",
            "payload": "/out_of_scope"
            }
        ]
        message = message + ' ' + '"' + title_intent + '"'  
        
        dispatcher.utter_message(text=message, buttons=buttons)

        return []

class ActionDefaultFallback(Action):
    
    def name(self) -> Text:
        return "action_default_fallback"
    
    def run(self, dispatcher, tracker, domain):
    
        dispatcher.utter_message(text="Lo lamento, no puedo ayudarte con eso.")
        dispatcher.utter_message(text="Recuerda que puedes escribir 'ayuda' para guiarte para guiarte en las principales temas y consultas sobre los cuales puedo responder")
        dispatcher.utter_message(response=f"utter_sugerir_contactar_aera")
        dispatcher.utter_message(response=f"utter_requerir_mas")

        return [ConversationPaused(), UserUtteranceReverted()]


class ValidateCourseScheduleForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_course_schedule_form"

    @staticmethod
    def course_db() -> List[Text]:
        """Database of supported cuisines"""
        allCourses = getCoursesAndCodes()
        #print('allCourses: ',allCourses)
        return allCourses

    @staticmethod
    def sections_db(course_code) -> List[Text]:
        sections = getSectionsCourseByCode(course_code)
        sections = [sec.lower() for sec in sections]
        return sections

    def validate_course(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate course value."""
        
        
        course_detail = None
        course_slot = None
        course_matches_slot = None
        section_slot = tracker.get_slot('section')
        course_code_slot = None
        
        slot_value = slot_value.strip()
        print('Course slot_value:', slot_value)

        #course_matches_slot = None
        courses = self.course_db()

        value_unaccent = unidecode.unidecode(slot_value)
        course_matches = [course for course in courses 
            if re.search(slot_value, course['nombre'], re.IGNORECASE) or re.search(value_unaccent, unidecode.unidecode(course['nombre']), re.IGNORECASE)]


        if len(course_matches) == 0:
                dispatcher.utter_message(text=f"Lo lamento no encontre algun curso que coincida con el nombre {slot_value}")


        exact_matches = [ course for course in course_matches if course['nombre'].lower() == slot_value.lower()]
        

        if len(exact_matches) == 1:
            # validation succeeded, set the value of the "cuisine" slot to value
            course_slot = exact_matches[0]['nombre']
            course_detail = exact_matches[0]
            course_code_slot = exact_matches[0]['codigo']
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            if len(course_matches) == 1:
                course_slot = course_matches[0]['nombre']
                course_detail = course_matches[0]
                course_code_slot = course_matches[0]['codigo']
            elif len(course_matches) >= 2:
                if len(course_matches)> 4:
                    course_matches = course_matches[:4]
                #SlotSet('courses_matches', matches)
                
                if slot_value != None: 
                    dispatcher.utter_message(text=f"Encontre varias opciones para el curso de {slot_value}")
                
                course_matches_slot = course_matches
        
        if course_slot!= None and course_detail!= None and section_slot == None:
            sections = getSectionsCourseByCode(course_detail['codigo'])
            if len(sections) == 1:
                section_slot = sections[0]
        
        print('course_code_slot: ', course_code_slot)

        return {
                "course": course_slot, 
                "courses_matches": course_matches_slot,
                "section": section_slot,
                "course_code": course_code_slot
                }

    def validate_section(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate course value."""
        
        section_slot = None
        section_matches_slot = None
        course_slot = tracker.get_slot('course')
        course_code = tracker.get_slot('course_code')

        sections = self.sections_db(course_code)
        
        if slot_value.lower() in sections:
            # validation succeeded, set the value of the "cuisine" slot to value
            section_slot = slot_value
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            dispatcher.utter_message(text=f"Lo siento el curso de {course_slot} no tiene secction {slot_value}")
            section_matches_slot = sections

        return {
                "section": section_slot, 
                "sections_matches": section_matches_slot,
                }

    async def required_slots(
        self, 
        slots_mapped_in_domain: List[Text], 
        dispatcher: "CollectingDispatcher", 
        tracker: "Tracker", 
        domain: "DomainDict"
        ) -> List[Text]:

        course_name = tracker.get_slot("course")
        courses_matches = tracker.get_slot('courses_matches')
        additional_slots = ['course_code']
        if course_name != None and  courses_matches != None:
            exact_matches = [ course['nombre'] == course_name.lower() for course in courses_matches]
            if len(exact_matches) >= 2:
                return additional_slots + slots_mapped_in_domain

        return await super().required_slots(slots_mapped_in_domain, dispatcher, tracker, domain)



class ValidateCourseRoomForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_course_room_form"

    @staticmethod
    def course_db() -> List[Text]:
        """Database of supported cuisines"""
        allCourses = getCoursesAndCodes()
        #print('allCourses: ',allCourses)
        return allCourses

    @staticmethod
    def sections_db(course_code) -> List[Text]:
        sections = getSectionsCourseByCode(course_code)
        sections = [sec.lower() for sec in sections]
        return sections

    def validate_course(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate course value."""
        
        
        course_detail = None
        course_slot = None
        course_matches_slot = None
        section_slot = tracker.get_slot('section')
        course_code_slot = None
        
        slot_value = slot_value.strip()
        print('Course slot_value:', slot_value)

        #course_matches_slot = None
        courses = self.course_db()

        value_unaccent = unidecode.unidecode(slot_value)
        course_matches = [course for course in courses 
            if re.search(slot_value, course['nombre'], re.IGNORECASE) or re.search(value_unaccent, unidecode.unidecode(course['nombre']), re.IGNORECASE)]


        if len(course_matches) == 0:
                dispatcher.utter_message(text=f"Lo lamento no encontre algun curso que coincida con el nombre {slot_value}")


        exact_matches = [ course for course in course_matches if course['nombre'].lower() == slot_value.lower()]
        

        if len(exact_matches) == 1:
            # validation succeeded, set the value of the "cuisine" slot to value
            course_slot = exact_matches[0]['nombre']
            course_detail = exact_matches[0]
            course_code_slot = exact_matches[0]['codigo']
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            if len(course_matches) == 1:
                course_slot = course_matches[0]['nombre']
                course_detail = course_matches[0]
                course_code_slot = course_matches[0]['codigo']
            elif len(course_matches) >= 2:
                if len(course_matches)> 4:
                    course_matches = course_matches[:4]
                #SlotSet('courses_matches', matches)
                
                if slot_value != None: 
                    dispatcher.utter_message(text=f"Encontre varias opciones para el curso de {slot_value}")
                
                course_matches_slot = course_matches
        
        if course_slot!= None and course_detail!= None and section_slot == None:
            sections = getSectionsCourseByCode(course_detail['codigo'])
            if len(sections) == 1:
                section_slot = sections[0]
        
        print('course_code_slot: ', course_code_slot)

        return {
                "course": course_slot, 
                "courses_matches": course_matches_slot,
                "section": section_slot,
                "course_code": course_code_slot
                }

    def validate_section(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate course value."""
        
        section_slot = None
        section_matches_slot = None
        course_slot = tracker.get_slot('course')
        course_code_slot = tracker.get_slot('course_code')
        sections = self.sections_db(course_code_slot)
        
        if slot_value.lower() in sections:
            # validation succeeded, set the value of the "cuisine" slot to value
            section_slot = slot_value
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            dispatcher.utter_message(text=f"Lo siento el curso de {course_slot} no tiene secction {slot_value}")
            section_matches_slot = sections

        return {
                "section": section_slot, 
                "sections_matches": section_matches_slot,
                }

    async def required_slots(
        self, 
        slots_mapped_in_domain: List[Text], 
        dispatcher: "CollectingDispatcher", 
        tracker: "Tracker", 
        domain: "DomainDict"
        ) -> List[Text]:

        course_name = tracker.get_slot("course")
        courses_matches = tracker.get_slot('courses_matches')
        additional_slots = ['course_code']
        if course_name != None and  courses_matches != None:
            exact_matches = [ course['nombre'] == course_name.lower() for course in courses_matches]
            if len(exact_matches) >= 2:
                return additional_slots + slots_mapped_in_domain

        return await super().required_slots(slots_mapped_in_domain, dispatcher, tracker, domain)


## Agregar el validate para secction

class ActionAskCourse(Action):
    def name(self) -> Text:
        return "action_ask_course"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        courses_matches = tracker.get_slot('courses_matches')
        slots = tracker.current_slot_values()
       
        last_intent = tracker.get_intent_of_latest_message()
        print('last_intent: ', last_intent)

        if courses_matches!= None and len(courses_matches)>=2:
            buttons = []
            for course in courses_matches:
                #payload = f'/{last_intent}{{"course": "{course["nombre"]}","course_code": "{course["codigo"]}"}}'
                payload = course["nombre"]
                buttons.append({ "title": course['nombre'], "payload": payload})
          
            dispatcher.utter_message(text=f"¿Cual es el curso al que te refieres?", buttons=buttons)
            SlotSet('courses_matches', None)
        else:
            dispatcher.utter_message(text="¿Cual es el curso?")
        return []

class ActionAskSection(Action):
    def name(self) -> Text:
        return "action_ask_section"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        course_slot = tracker.get_slot('course')
        course_code = tracker.get_slot('course_code')
        sections = getSectionsCourseByCode(course_code)

        print('section course_slot:', course_slot)
        print('section course_code:', course_code)
        print(sections)
        
        last_intent = tracker.get_intent_of_latest_message()
        print('Seccion last_intent: ', last_intent)

        if sections!= None and len(sections)>=2:
            buttons = [
                { 
                "title": section, 
                "payload": section#f'/horario_curso{{"section": "{section}"}}'
                } 
                for section in sections 
            ]
            dispatcher.utter_message(text=f"¿A cual seccion te refieres", buttons=buttons)
        else:
            dispatcher.utter_message(text="¿Cual es la seccion?")
        return []

class ActionAskCourseCode(Action):
    def name(self) -> Text:
        return "action_ask_coursecode"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        course_slot = tracker.get_slot('course')
        courses_matches = tracker.get_slot('courses_matches')
        print('courses_matches course_slot:', courses_matches)
        if courses_matches!= None and len(courses_matches)>=2:
            buttons = [
                { 
                "title": course['nombre'] + '('+ course['codigo'] + ')', 
                "payload": course["codigo"]#f'/cursos_horarios{{"course_code": "{course["codigo"]}"}}'
                } 
                for course in courses_matches 
            ]
            dispatcher.utter_message(text=f"Encontre dos cursos con el mismo nombre, ¿A cual te refieres?", buttons=buttons)
        else:
            dispatcher.utter_message(text="¿Cual es el codigo del curso?")
        return []

class ActionFindCourseSchedule(Action):
    def name(self) -> Text:
        return "action_find_course_schedule"

    def run(self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict) -> List[Dict[Text, Any]]:
        course = tracker.get_slot('course')
        course_code = tracker.get_slot('course_code')
        section = tracker.get_slot('section')
        schedule = getCourseSchedule(course_code, section)
        print(schedule)
        utter = f'el curso de {course.lower()} en la seccion {section.upper()} se dicta los dias: '
        for idx, cls in enumerate(schedule):
            utter = utter + cls['dia'] + " clase de " + cls['tipo_clase'] + " de " + cls['empieza_en'] + " a " + cls['termina_en']
            print(idx)
            if len(schedule)> 1 and (idx + 2) == len(schedule):
                utter = utter + " y "
            else:
                if((idx + 1) == len(schedule)):
                    utter = utter + "."
                else:
                    utter = utter + ", "  
        
        dispatcher.utter_message(text= utter)
        return [AllSlotsReset()]


class ActionFindCourseRoom(Action):
    def name(self) -> Text:
        return "action_find_course_room"

    def run(self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict) -> List[Dict[Text, Any]]:
        course = tracker.get_slot('course')
        course_code = tracker.get_slot('course_code')
        section = tracker.get_slot('section')
        course_rooms = getCourseRoom(course_code, section)
        print(course_rooms)
        
        presencial_clases = [cr for cr in course_rooms if not re.search('zoom', cr['aula'], re.IGNORECASE)]

        
        utter = f'el curso de {course.lower()} en la seccion {section.upper()} se dicta de manera presencial los dias: 'if len(presencial_clases) > 0 else f'El curso de {course.lower()} debido a la coyuntura actual no se esta dictando presencialmente, revise su correo instucional o consulta con su docente por los accesos para sus clases'
        
        for idx, cls in enumerate(presencial_clases):

            utter = utter + cls['dia'] + " en el aula " + cls['aula'] + " de " + cls['empieza_en'] + " a " + cls['termina_en'] + " clase de " + cls['tipo_clase']
            print(idx)
            if len(course_rooms)> 1 and (idx + 2) == len(course_rooms):
                utter = utter + " y "
            else:
                if((idx + 1) == len(course_rooms)):
                    utter = utter + "."
                else:
                    utter = utter + ", "  
        
        dispatcher.utter_message(text= utter)
        aulas = [clase['aula'] for clase in presencial_clases]

        return [SlotSet('aulas_course', aulas), SlotSet('course', None), SlotSet('course_code', None), 
                SlotSet('section', None), SlotSet('courses_matches')]

class ActionFindCourseRoomsUbication(Action):
    def name(self) -> Text:
        return "action_find_course_rooms_ubication"

    def run(self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict) -> List[Dict[Text, Any]]:
        

        aulas = tracker.get_slot('aulas_course')
        
        j3_aulas = [ aula for aula in aulas if re.search('^J', aula, re.IGNORECASE) ]
        
        first_floor_j3 = [j3_aula for j3_aula in j3_aulas if re.search('^(J3(\s|\-)?1)', j3_aula, re.IGNORECASE)]
        
        second_floor_j3 = [j3_aula for j3_aula in j3_aulas if re.search('^(J3(\s|\-)?2)', j3_aula, re.IGNORECASE)]

        
        r_aulas = [ aula for aula in aulas if re.search('^R\d?', aula, re.IGNORECASE) ]

        if len(j3_aulas) >0 :
            if len(j3_aulas) == 1:
                utter = 'El aula ' + j3_aulas[0] + " se ubica"
                if len(first_floor_j3) > 0:
                    utter = utter + ' en el primer piso del Pabellon J'
                elif len(second_floor_j3) > 0:
                    utter = utter + ' en el segundo piso del Pabellon J'
                else:
                    utter = utter + ' Pabellon J.'
            else:    
                utter = "Las aulas " + " ".join(j3_aulas[:-1]) + " y " +  j3_aulas[-1] + ' se ubican dentro del Pabellon J.'
                if len(first_floor_j3) > 0:
                    utter = utter + "El aula" + j3_aulas [0] if len(j3_aulas) == 1 else "Las aulas " + " ".join(j3_aulas[:-1]) + " y " +  j3_aulas[-1]
                    utter = utter + ' en el primer piso'

                if (len(second_floor_j3)) >0:
                    utter = utter + "y" if len(first_floor_j3) >0 else utter
                    utter = utter + "El aula " + j3_aulas [0] if len(j3_aulas) == 1 else "Las aulas " + " ".join(j3_aulas[:-1]) + " y " +  j3_aulas[-1]
                    utter = utter + ' en el segundo piso'

            dispatcher.utter_message(text=utter)
            dispatcher.utter_message(text = 'Puede ver la localizacion del Pabellon J en el siguiente enlace: https://goo.gl/maps/TcVSodUAGDWxPyCZ7')
            

        floors = ['primer', 'segundo', 'tercero', 'cuarto']

        if len(r_aulas) > 0 :

            if len(r_aulas) == 1:
                utter = 'El aula ' + r_aulas[0] + " se ubica"
                floor = None
                for i in range(1,5):
                    if re.search(f'^(R\d(\s|\-)?{i})', r_aulas[0], re.IGNORECASE):
                        floor = floors[i - 1]
                if floor != None:
                    utter = utter + f' en el {floor} piso del Pabellon J'
                else:
                    utter = utter + ' Pabellon J.'
            else:
                utter = "Las aulas " + " ".join(r_aulas[:-1]) + " y " +  r_aulas[-1] + ' se ubican dentro del Pabellon R.'
                floors_r = [
                            [
                            r_aula for r_aula in r_aulas 
                                if re.search(f'^(R\d(\s|\-)?{i})', r_aula, re.IGNORECASE)
                            ] for i in range(1,5)
                        ] 
                for idx , floor_r in enumerate(floors_r):
                    if len(floor_r) > 0:
                        if(idx == 0):
                            utter = utter + " El aula " + floor_r[0] if len(floor_r) == 1 else "Las aulas " + " ".join(j3_aulas[:-1]) + " y " +  floor_r[-1]
                            floor = floors[idx]
                            utter = utter + f' en el {floor} piso'
                        else:
                            utter = utter + "y" if len(floor_r) >0 else utter
                            utter = "El aula " + floor_r[0] if len(floor_r) == 1 else "Las aulas " + " ".join(floor_r[:-1]) + " y " +  floor_r[-1]
                            floor = floors[idx]
                            utter = utter + f' en el {floor} piso' 

            dispatcher.utter_message(text=utter)
            dispatcher.utter_message(text = 'Puede ver la localizacion del Pabellon R en el siguiente enlace: https://goo.gl/maps/HTo4V4qZCRGdUBRm7')

        return [AllSlotsReset()]



class ActionFindRoomUbication(Action):
    def name(self) -> Text:
        return "action_find_room_ubication"

    def run(self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: DomainDict) -> List[Dict[Text, Any]]:
        
        aula =  tracker.latest_message['entities'][0]['value']
        
        floors = ['primer', 'segundo', 'tercero', 'cuarto']
        print(aula)

        if re.search('^J', aula, re.IGNORECASE):
            utter = "El aula " + aula + ' se encuentra'
            for idx in range(1,3):
                 if re.search(f'^(J3(\s|\-)?{idx})', aula, re.IGNORECASE):
                    floor = floors[idx - 1]
                    utter = utter + f' en el {floor} piso'
                    break

            utter = utter + ' dentro del Pabellon J.'

            dispatcher.utter_message(text=utter)
            dispatcher.utter_message(text = 'Puede ver la localizacion del Pabellon J en el siguiente enlace: https://goo.gl/maps/TcVSodUAGDWxPyCZ7')

        if re.search('^R\d?', aula, re.IGNORECASE):
            utter = "El aula " + aula + ' se encuentra'
            for idx in range(1,5):
                 if re.search(f'^(R\d(\s|\-)?{idx})', aula, re.IGNORECASE):
                    floor = floors[idx -1]
                    utter = utter +  f' en el {floor} piso'
                    break
            
            utter = utter + ' dentro del Pabellon R.' 
                 
            dispatcher.utter_message(text=utter)
            dispatcher.utter_message(text = 'Puede ver la localizacion del Pabellon R en el siguiente enlace: https://goo.gl/maps/HTo4V4qZCRGdUBRm7')
        
        return []
#class ActionContextualFaqsFormatoSolicitud(Action):
#    """Returns the chitchat utterance dependent on the intent"""
#
#    def name(self) -> Text:
#        return "action_contextual_faq_formato_solicitud"

#    def run(
#        self,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> List[EventType]:
#        sub_topic = tracker.get_slot("sub_topic")
#        print(sub_topic, 'sub_topic')
#        if sub_topic in ["retiro_total", "reincorporacion", "reserva_matricula","constancia_de_estudios","constancia_matricula"]:
#            dispatcher.utter_message(response=f"utter_{sub_topic}__formato_solicitud")
#        else:
#            dispatcher.utter_message(text="Lo lamento no tengo esa información")#
#
#        return []


#class ActionSetSubTopicSlot(Action):
#    """Returns the chitchat utterance dependent on the intent"""
#
#    def name(self) -> Text:
#        return "action_set_sub_topic_slot"
#
#    def run(
#        self,
#       dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> List[EventType]:
#        full_intent = (
#            tracker.latest_message.get("response_selector", {})
#            .get("faq", {})
#            .get("response",{})
#            .get("intent_response_key")
#        )
#        print('full_intent:', full_intent)
#        if full_intent:
#            topic = full_intent.split("/")[1]
#            print('topic: ', topic)
#            sub_topic = topic.split("__")[0]
#        else:
#            sub_topic = None
#        print('sub_topic:', sub_topic)
#        return [SlotSet("sub_topic", sub_topic)]